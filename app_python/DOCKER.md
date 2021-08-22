## Best practices for Docker
1. Create ephemeral containers
2. Understand build context
3. Pipe Dockerfile through `stdin`
4. Build an image using a Dockerfile from `stdin`, without sending build context
5. Build from a local build context, using a Dockerfile from `stdin`
6. Build from a remote build context, using a Dockerfile from `stdin`
7. Exclude with .dockerignore
8. Use multi-stage builds
9. Don’t install unnecessary packages
10. Decouple applications
11. Minimize the number of layers
12. Sort multi-line arguments
13. Leverage build cache