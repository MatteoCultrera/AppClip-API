if [ $# -ne 2 ]; then
   echo "add the token with -t" >&2
   exit 1
fi

if [ "$1" != "-t" ]; then
  echo "add the token with -t" >&2
  exit 1
fi

TOKEN=$2

cd api
sed -i .bak "s/^token=.*/token='$TOKEN'/g" index.py
rm index.py.bak

cd ..
git commit -a -m "Update Token"
git push
