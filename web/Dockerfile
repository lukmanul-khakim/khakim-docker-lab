FROM nginx:alpine

LABEL org.opencontainers.image.title="KHAKIM LAB"
LABEL org.opencontainers.image.description="KHAKIM LAB Portofolio Web Image"

COPY src/ /usr/share/nginx/html/

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 CMD wget -q --spider http://127.0.0.1/ || exit 1
