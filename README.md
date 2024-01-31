# Actions

This repo contains actions and workflow files for [GitHub Actions](https://github.com/features/actions).
It also contains example workflow files for inclusion in other repos which call the GitHub actions defined in this repo.

We aim to improve developer efficiency by giving them tools to enable good practices that are easy to integrate, so they can spend more time focusing on writing code, and less on setting up checks.

## Action Groups summary

* R (`R.yml`): Checks related to the R programming language.
* Docker (`docker.yml`): actions related to checking and building Docker images
* General (`general.yml`): Actions to run on all repositories, regardless of languages involved

## Structure

The workflows are `*.yml` files in `.github/workflows/`, with all files in that directory (no nesting).
The workflow files have names with the group of workflow as a prefix (ex. `R-*.yml` would be an action for R code, `docker-*.yml` would relate to docker containers).
Files that do not have a prefix are "caller" workflows, which call the other workflows in turn (ex. `R.yml` would call `R-*.yml` workflows), to simplify managment from other repositories (a repo containing an R package can call `R.yml`, to enable all actions called by that file).

## Action Group Details

### R (`R.yml`)

* lintr: runs `lintr::lint_package()` with [default configuration](https://lintr.r-lib.org/articles/lintr.html#configuring-linters) (`lintr::default_linters()` for repos that do not have a `.lintr` file)
* codecov: checks test coverage (using `covr`) and uploads results to codecov.io
