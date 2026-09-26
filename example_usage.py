import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import PersonalCircadianEnergySchedulerClient

def main():
    client = PersonalCircadianEnergySchedulerClient()
    res = client.align_circadian_tasks()
    print("=== Personal Circadian Energy Scheduler Output ===")
    print(f"User: {res['user_name']} | Chronotype: {res['detected_chronotype'].upper()}")
    print(f"Biological Prime Time: {res['biological_prime_time']} | Circadian Trough: {res['vulnerability_trough_window']}")
    print(f"Sync Score: {res['circadian_sync_score'] * 100}%")
    print("\nOptimal Task Mappings:")
    for item in res['aligned_task_itinerary']:
        print(f"  * [{item['recommended_optimal_slot']}] {item['task']} -> {item['expected_efficiency_multiplier']}")

if __name__ == '__main__':
    main()
