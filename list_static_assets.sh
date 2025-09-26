#!/bin/bash
# list_static_assets.sh

echo "📦 Static assets in /static:"
find static -type f \
    ! -name '.*' \
    ! -name 'Thumbs.db' \
    ! -name '.DS_Store' \
    | sed 's|^static/||' \
    | sort
