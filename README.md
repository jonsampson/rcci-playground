# rcci-playground

Price checking over time for a certain cruise.

## Run

```sh
poetry run python -m rcci_playground
```

## Crontab entry

Sample once daily at 6AM.

```
0 6 * * * /usr/bin/zsh -l -c ". $HOME/.zshrc ; cd <REPO_DIR> ; export DISPLAY=:1 ; poetry run -C <REPO_DIR> python -m rcci_playground"
```