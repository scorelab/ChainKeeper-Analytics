import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

from datetime import timedelta


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(0),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'Bitcoin Data Crawlers',
    default_args=default_args,
    description='Bit coin data gathering',
    schedule_interval=timedelta(days=1),
)


spider1 = BashOperator(
    task_id='bitcoinabuse',
    bash_command='python "$HOME/ChainKeeper-Analytics/crawlers/bitcoinabuse crawlers/bitcoinabuse.py"',
    dag=dag,
)


spider2 = BashOperator(
    task_id='BitcoinFog spider',
    depends_on_past=False,
    bash_command='python "$HOME/ChainKeeper-Analytics/crawlers/walletexplorer crawlers/BitcoinFog spider.py"',
    dag=dag,
)

spider3 = BashOperator(
    task_id='BitLaunder.com spider',
    bash_command='python "$HOME/ChainKeeper-Analytics/crawlers/walletexplorer crawlers/BitLaunder.com spider.py"',
    dag=dag,
)


spider4 = BashOperator(
    task_id='HelixMixer spider',
    depends_on_past=False,
    bash_command='python "$HOME/ChainKeeper-Analytics/crawlers/walletexplorer crawlers/HelixMixer spider.py"',
    dag=dag,
)


if __name__ == '__main__':
 spider1>>spider2>>spider3>>spider3
