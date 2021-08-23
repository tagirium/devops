## Best practices for Docker
1. Avoid running containers as root.
2. Don’t bind to a specific UID.
3. Make executables owned by root and not writable.
4. Leverage multistage builds.
5. Use distroless images, or build your own from scratch.
6. Update your images frequently.
7. Watch out for exposed ports.
8. Never put secrets or credentials in Dockerfile instructions.
9. Prefer COPY over ADD.
10. Be aware of the Docker context, and use `.dockerignore`.
11. Reduce the number of layers, and order them intelligently.
12. Add metadata and labels.
13. Leverage linters to automatize checks.
14. Scan your images locally during development.
15. Protect the docker socket and TCP connections.
16. Sign your images, and verify them on runtime.
17. Avoid tag mutability.
18. Don’t run your environment as root.
19. Include a health check.
20. Restrict your application capabilities.