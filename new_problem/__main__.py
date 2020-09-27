from typing import *
import os
import argparse
import pathlib
from string import Template
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("owner", help="problem owner", type=str)
parser.add_argument("id", help="id of problem", type=str)

args = parser.parse_args()

problem_name: str = "{}_{}".format(args.owner, args.id)

owner_path = pathlib.Path(args.owner)
templates_dir_origin = pathlib.Path("./templates")

ows = list(map(lambda x: x.name, list(templates_dir_origin.iterdir())))

templates_name = "default" if args.owner not in ows else args.owner

templates_dir = templates_dir_origin / templates_name

if not owner_path.exists():
    os.mkdir(owner_path)

problem_path = owner_path / problem_name

if not problem_path.exists():
    os.mkdir(problem_path)


def _iter_dir(path):
    for child_item in path.iterdir():
        # 하위 폴더
        if child_item.is_dir():
            target_child_path = problem_path / child_item.name
            if not target_child_path.exists():
                os.mkdir(target_child_path)

            _iter_dir(child_item)

        elif child_item.name.endswith(".template"):
            t = Template(child_item.name)
            target_name = t.substitute(problem_name=problem_name)
            target_name = target_name.replace(".template", "")
            target_file_path = (
                problem_path
                / child_item.relative_to(templates_dir).parent
                / target_name
            )

            with open(child_item, mode="r", encoding="utf-8") as tf_a, open(
                target_file_path, mode="w", encoding="utf-8"
            ) as tf_b:
                for ln in tf_a.readlines():
                    t = Template(ln)
                    tf_b.writelines(t.substitute(problem_name=problem_name))

        else:
            shutil.copyfile(child_item, problem_path / path.name / child_item.name)


_iter_dir(templates_dir)
