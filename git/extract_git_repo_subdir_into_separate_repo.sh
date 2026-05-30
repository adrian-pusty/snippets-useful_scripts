#todo to be tested

path_to_big_repo=/path/to/big/repo  #todo
path_to_subdir="$path_to_big_repo"/some/subdir  #todo
path_to_extracted_repo=/path/to/extracted/repo  #todo

subdir_branch=some_name #todo


cd "$path_to_big_repo" || exit
git subtree split -P "$path_to_subdir" -b "$subdir_branch"
mkdir "$path_to_extracted_repo" && cd "$path_to_extracted_repo"
git init
git pull "$path_to_big_repo" "$subdir_branch"