## CI best practices
Maintain a code repository

Automate the build

Make the build self-testing

Everyone commits to the baseline every day

Every commit (to baseline) should be built

Keep the build fast

Test in a clone of the production environment

Make it easy to get the latest deliverables

Everyone can see the results of the latest build

Automate deployment

## Jenkins best practices
Making sure to use Groovy code in Pipelines as glue

Avoiding complex Groovy code in Pipelines

Reducing repetition of similar Pipeline steps

Avoiding calls to Jenkins.getInstance

Do not override built-in Pipeline steps

Avoiding large global variable declaration files

Avoiding very large shared libraries

## Problems with Jenkins
When Jenkins was running as Docker container, it couldn't connect to docker to pull any images, so I downloaded another
version of it. After this I faced another problem connected with OS I amusing (Windows) - all images that
Docker have Linux paths. Using Docker Desktop they are automatically converting, but not when I used Docker in Jenkins.
Because of this, I couldn't access any of agents that I was in need of. 