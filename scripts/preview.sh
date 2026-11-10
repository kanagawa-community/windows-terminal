# Preview hook for .github/scripts/render-previews.sh: Windows Terminal does not run on
# Linux, so the shared session (scripts/session.sh in the .github repository)
# runs in a headless tmux pane instead, and termframe draws the capture with the
# variant's background, foreground and 16 terminal colors. These are the same
# roles that the Windows Terminal theme uses.
# Requires: tmux, eza, fastfetch, rsync.
# shellcheck shell=bash
name=windows-terminal

setup() {
  # The listing shows this repository's own files, copied into a fixed home
  # directory with one timestamp, so only the file names and sizes change.
  demo="$work/home/kanagawa-community/$(basename "$root")"
  mkdir -p "$demo"
  rsync -a --exclude=.git --filter=":- .gitignore" "$root"/ "$demo"/
  mkdir "$demo/.git"
  find "$demo" -exec touch -h -d '2026-11-07 11:13' {} +
}

cleanup() {
  tmux -L kanagawa-preview kill-server 2>/dev/null || true
}

capture() {
  cleanup
  sleep 0.5
  tmux -L kanagawa-preview new-session -d -s s -x 100 -y 30 \
    -e HOME="$work/home" -e USER=kanagawa -e COLORTERM=truecolor \
    -e TERM=xterm-256color -e LC_ALL=C.UTF-8 -e LESS= -e LESSOPEN= \
    "bash $here/session.sh $demo $1"
  sleep 2
  tmux -L kanagawa-preview capture-pane -p -e -t s >"$2"
}
