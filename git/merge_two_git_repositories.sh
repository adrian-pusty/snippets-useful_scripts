target_project_path=/path/to/target/project #todo
source_project_path=/path/to/source/project #todo
source_project_branch=master #todo

cd "$source_project_path" || exit
git checkout "$source_project_branch"

cd "$target_project_path" || exit
git remote add source-project "$source_project_path"
git fetch source-project --tags
git merge --allow-unrelated-histories source-project/"$source_project_branch"
git remote remove source-project
