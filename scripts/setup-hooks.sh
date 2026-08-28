#!/bin/sh
# setup git hooks for auto push (run once per clone)
cat > .git/hooks/post-commit << 'HOOK'
#!/bin/sh
if git remote | grep -q origin; then
  git push --quiet &
fi
HOOK
chmod +x .git/hooks/post-commit
echo "hook installed: post-commit -> git push"
