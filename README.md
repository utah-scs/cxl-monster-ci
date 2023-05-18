This is a CloudLab profile designed to allocate a small cluster, initialize
passwordless ssh between all of the nodes, and then start a Github CI Runner on
one of the nodes to accept enqueued work from Github actions.

It builds on Leigh's [example repository-based CloudLab
profile](https://github.com/lbstoller/my-profile).

This repository can be (and is) configured with a Webhook to automatically push
changes to this profile to the corresponding profile on CloudLab.

# Configuration

The code that establishes the runner is fairly generic and should work for any
project that wants to accept work from Github CI Actions.
`setup-github-ci-runner.sh` needs to pointed at the repo for which the runner
should accept actions. It must also be pointed at a file that contains the
registration token string that Github provides when the action is created on
the Github project.

After that, jobs/actions can be specified in Github and an instance of this
profile should pick up any enqueued actions and perform them.
