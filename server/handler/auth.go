package handler

import (
	"crypto/subtle"
	"net/http"
)

func AuthMiddleware(token string) func(http.Handler) http.Handler {
	return func(next http.Handler) http.Handler {
		return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
			if token == "" {
				next.ServeHTTP(w, r)
				return
			}

			// Check query param ?token=xxx
			qt := r.URL.Query().Get("token")
			if qt != "" && subtle.ConstantTimeCompare([]byte(qt), []byte(token)) == 1 {
				next.ServeHTTP(w, r)
				return
			}

			// Check Authorization: Bearer header
			ah := r.Header.Get("Authorization")
			if len(ah) > 7 && ah[:7] == "Bearer " {
				bt := ah[7:]
				if subtle.ConstantTimeCompare([]byte(bt), []byte(token)) == 1 {
					next.ServeHTTP(w, r)
					return
				}
			}

			w.Header().Set("Content-Type", "application/json")
			w.WriteHeader(http.StatusUnauthorized)
			w.Write([]byte(`{"error":"unauthorized"}`))
		})
	}
}
