from menutime import app
import os
from menutime import db
from menutime.models import Meal_Details

# db.create_all()


if __name__ == "__main__":
    app.run(ssl_context='adhoc', host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=80, debug=True)
