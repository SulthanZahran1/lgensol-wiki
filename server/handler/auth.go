package handler

import (
	"crypto/subtle"
	"encoding/json"
	"net/http"
	"os"
)

// AccessToken returns the configured access token from env or empty string.
func AccessToken() string {
	return os.Getenv("ACCESS_TOKEN")
}

// ApiAuthMiddleware wraps a handler to require access token on API routes.
// It checks query param `?token=` or header `Authorization: Bearer <token>`.
// If ACCESS_TOKEN is empty, auth is disabled entirely.
func ApiAuthMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		token := AccessToken()
		if token == "" {
			next.ServeHTTP(w, r)
			return
		}

		provided := r.URL.Query().Get("token")
		if provided == "" {
			if h := r.Header.Get("Authorization"); len(h) > 7 && h[:7] == "Bearer " {
				provided = h[7:]
			}
		}

		if provided == "" || subtle.ConstantTimeCompare([]byte(provided), []byte(token)) != 1 {
			w.Header().Set("Content-Type", "application/json")
			w.WriteHeader(http.StatusUnauthorized)
			json.NewEncoder(w).Encode(map[string]string{
				"error":   "unauthorized",
				"message": "Provide ?token=<access_token> or Authorization: Bearer <token>",
			})
			return
		}

		next.ServeHTTP(w, r)
	})
}

// StaticAuthMiddleware checks token header/query for API calls,
// but allows OPTIONS (CORS preflight) and lets the handler decide for others.
// Not used currently — we use ApiAuthMiddleware on the API sub-mux instead.
func StaticAuthMiddleware(next http.Handler) http.Handler {
	return next
}