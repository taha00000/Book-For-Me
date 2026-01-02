"""
Verify the recent booking: Smash Padel Clifton, Dec 15, 2025, 12:00 PM
"""
import asyncio
import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.dirname(script_dir)
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from app.firestore import firestore_db
from google.cloud.firestore_v1.base_query import FieldFilter

async def verify_booking():
    print("\n" + "=" * 70)
    print("VERIFYING RECENT BOOKING STATUS")
    print("=" * 70)
    print("\nLooking for:")
    print("  Vendor: smash_padel_clifton")
    print("  Date: 2025-12-15")
    print("  Time: 12:00 (12 PM)")
    print("\n" + "-" * 70)
    
    query = firestore_db.db.collection('slots')\
        .where(filter=FieldFilter('vendor_id', '==', 'smash_padel_clifton'))\
        .where(filter=FieldFilter('date', '==', '2025-12-15'))\
        .limit(50)
    
    docs = list(query.stream())
    print(f"\nFound {len(docs)} slots for smash_padel_clifton on 2025-12-15\n")
    
    found_target = False
    
    for doc in docs:
        data = doc.to_dict()
        start_time = data.get('start_time')
        
        if start_time:
            if hasattr(start_time, 'strftime'):
                time_str = start_time.strftime('%H:%M')
            else:
                time_str = str(start_time)[:5] if len(str(start_time)) >= 5 else str(start_time)
        else:
            time_str = 'N/A'
        
        status = data.get('status', 'unknown')
        
        if time_str == '12:00':
            found_target = True
            print(f">>> TARGET SLOT FOUND (12:00 PM):")
            print(f"   Slot ID: {doc.id}")
            print(f"   Status: {status.upper()}")
            print(f"   Time: {time_str}")
            print(f"   Vendor ID: {data.get('vendor_id', 'N/A')}")
            print(f"   Date: {data.get('date', 'N/A')}")
            
            if status == 'confirmed':
                print(f"\n   ✅ [SUCCESS] STATUS IS CONFIRMED!")
                print(f"   Customer Name: {data.get('customer_name', 'N/A')}")
                print(f"   Customer Phone: {data.get('customer_phone', 'N/A')}")
                print(f"   Booking Source: {data.get('booking_source', 'N/A')}")
                print(f"   Updated At: {data.get('updated_at', 'N/A')}")
            else:
                print(f"\n   ❌ [FAILED] STATUS IS '{status.upper()}' (Expected: confirmed)")
                print(f"   This means the booking was NOT written to database correctly!")
            
            print()
            break
    
    if not found_target:
        print("[X] 12:00 PM slot NOT FOUND!")
        print("   Checking all slots for this date...")
        for doc in docs[:10]:
            data = doc.to_dict()
            start_time = data.get('start_time')
            if start_time and hasattr(start_time, 'strftime'):
                time_str = start_time.strftime('%H:%M')
            else:
                time_str = str(start_time)[:5] if start_time else 'N/A'
            status = data.get('status', 'unknown')
            print(f"   - {time_str}: {status}")
    
    print("=" * 70)

if __name__ == "__main__":
    asyncio.run(verify_booking())