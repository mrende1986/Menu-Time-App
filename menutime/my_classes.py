from menutime import db
import matplotlib.pyplot as plt
from google.cloud.firestore_v1 import aggregation
from google.cloud.firestore_v1.base_query import FieldFilter
from io import BytesIO


class Query:
    def __init__(self):
        self.db = db

    def query_num_menus(self):
        ## Query number of menus in DB
        collection_ref = db.collection("selections")
        query = collection_ref.where(filter=FieldFilter("created_date", "!=", ""))
        aggregate_query = aggregation.AggregationQuery(query)
        aggregate_query.count(alias="all")

        menu_results = aggregate_query.get()
        for result in menu_results:
            count_of_menus = result[0].value
        return count_of_menus

    def query_num_meals(self):
        ## Query number of meals in DB
        collection_ref = db.collection("meals")
        query = collection_ref.where(filter=FieldFilter("category", "!=", ""))
        aggregate_query = aggregation.AggregationQuery(query)
        aggregate_query.count(alias="all")

        meal_results = aggregate_query.get()
        for result in meal_results:
            count_of_meals = result[0].value
        return count_of_meals
    
    def run_query_and_plot(self):
        

        meal_names_query = self.db.collection("meals")
        meals = [doc.to_dict() for doc in meal_names_query.stream()]

        # Assuming each meal dictionary has a 'category' key
        category_counts = {}
        for meal in meals:
            category = meal['category']
            if category in category_counts:
                category_counts[category] += 1
            else:
                category_counts[category] = 1

        labels = list(category_counts.keys())
        counts = list(category_counts.values())

        # Use a non-interactive backend to avoid GUI issues in threads
        plt.switch_backend('Agg')

        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(labels, counts, color=plt.get_cmap('Pastel2').colors)
        ax.set_xlabel('Categories')
        ax.set_title('Number of Meals Currently Available by Category')

        # Apply spine and tick formatting
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_color('#DDDDDD')
        ax.tick_params(bottom=False, left=False)

        # Add horizontal grid lines
        ax.set_axisbelow(True)
        ax.yaxis.grid(True, color='#EEEEEE')
        ax.xaxis.grid(False)

        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom')  # va: vertical alignment

        # Instead of saving the plot, return it as a response object that can be used in Flask
        img = BytesIO()
        plt.savefig(img, format='png', bbox_inches='tight')
        plt.close(fig)
        img.seek(0)
        return img
