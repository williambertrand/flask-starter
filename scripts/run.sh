export FLASK_DEBUG=0

FLD="$( cd "$(dirname "$0")" ; pwd -P )"
. "$FLD/configuration.sh"

flask run --host=0.0.0.0