FROM golang:1.26-alpine AS builder
WORKDIR /app
COPY . .
RUN GOFLAGS="-mod=mod" go build -o wiki-server .

FROM alpine:3.21
RUN apk add --no-cache ca-certificates
COPY --from=builder /app/wiki-server /app/
COPY --from=builder /app/static/ /app/static/
COPY --from=builder /app/data/ /app/data/
ENV WIKI_DIR=/wiki
ENV GRAPH_PATH=/app/data/graph.json
ENV PORT=8080
EXPOSE 8080
WORKDIR /app
CMD ["./wiki-server"]