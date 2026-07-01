import os
import pickle
import numpy as np
import sqlite3

def run_verification():
    print("=== AgroYaar Integration Verification ===")
    
    # ----------------- 1. Check Model Files -----------------
    print("\nChecking asset binaries...")
    model_pkl = 'model/model.pkl'
    disease_h5 = 'model/disease_model.h5'
    class_pkl = 'model/class_names.pkl'
    
    for fpath in [model_pkl, disease_h5, class_pkl]:
        if not os.path.exists(fpath):
            print(f"[-] ERROR: Required model file '{fpath}' is missing! Run generate_assets.py first.")
            return False
        print(f"[+] Found: {fpath}")
        
    # ----------------- 2. Test Recommendation Model -----------------
    print("\nTesting Crop Recommendation Model...")
    try:
        with open(model_pkl, 'rb') as f:
            rec_payload = pickle.load(f)
            
        clf = rec_payload['model']
        le_d = rec_payload['encoder_district']
        le_t = rec_payload['encoder_taluka']
        le_s = rec_payload['encoder_soil']
        le_se = rec_payload['encoder_season']
        le_y = rec_payload['encoder_crop']
        
        # Mock inputs
        d_enc = le_d.transform(['Pune'])[0]
        t_enc = le_t.transform(['Haveli'])[0]
        s_enc = le_s.transform(['Clayey'])[0]
        se_enc = le_se.transform(['Kharif'])[0]
        
        pred_enc = clf.predict([[d_enc, t_enc, s_enc, se_enc]])[0]
        crop_name = le_y.inverse_transform([pred_enc])[0]
        
        print(f"[+] Recommendation success: Predicted crop for (Pune, Haveli, Clayey, Kharif) -> '{crop_name}'")
    except Exception as e:
        print(f"[-] ERROR in crop recommendation test: {e}")
        return False

    # ----------------- 3. Test Disease Detection Model -----------------
    print("\nTesting TensorFlow Disease Model loading and inference...")
    try:
        import tensorflow as tf
        
        # Load model and classes
        model = tf.keras.models.load_model(disease_h5)
        with open(class_pkl, 'rb') as f:
            class_names = pickle.load(f)
            
        print(f"[+] Successfully loaded Keras model and {len(class_names)} classes.")
        
        # Run dummy inference
        dummy_img = np.random.rand(1, 224, 224, 3)
        predictions = model.predict(dummy_img)
        pred_idx = np.argmax(predictions[0])
        predicted_disease = class_names[pred_idx]
        confidence = float(predictions[0][pred_idx]) * 100
        
        print(f"[+] Inference success: Predicted class '{predicted_disease}' (Conf: {confidence:.2f}%)")
    except Exception as e:
        print(f"[-] ERROR in TensorFlow disease model test: {e}")
        return False

    # ----------------- 4. Test Database Operations -----------------
    print("\nTesting SQLite Database Operations...")
    try:
        import database
        database.init_db()
        
        # Add test scan
        test_path = 'static/uploads/test_leaf.jpg'
        scan_id = database.add_scan(
            image_path=test_path,
            disease_key='tomato_early_blight',
            crop_name='Tomato',
            confidence=98.5,
            severity='Medium'
        )
        print(f"[+] Successfully inserted scan record with ID: {scan_id}")
        
        # Retrieve scan
        record = database.get_scan(scan_id)
        if not record:
            raise ValueError("Could not retrieve inserted scan record.")
            
        assert record['disease_key'] == 'tomato_early_blight'
        assert record['confidence'] == 98.5
        print("[+] Database read/write verified.")
        
        # Clean up database entry
        conn = database.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM scans WHERE id = ?", (scan_id,))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"[-] ERROR in database test: {e}")
        return False

    # ----------------- 5. Test PDF Report Generation -----------------
    print("\nTesting PDF Report Generation (ReportLab)...")
    try:
        # Generate dummy report
        from reportlab.lib.pagesizes import letter
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
        from reportlab.lib.styles import getSampleStyleSheet
        
        pdf_test_path = 'static/uploads/test_pdf_report.pdf'
        doc = SimpleDocTemplate(pdf_test_path, pagesize=letter)
        styles = getSampleStyleSheet()
        story = [
            Paragraph("AgroYaar PDF Test Report", styles['Heading1']),
            Spacer(1, 10),
            Paragraph("This is a verification document.", styles['Normal'])
        ]
        doc.build(story)
        
        if not os.path.exists(pdf_test_path):
            raise FileNotFoundError("PDF file was not created.")
            
        os.remove(pdf_test_path)
        print("[+] PDF Generation verified.")
    except Exception as e:
        print(f"[-] ERROR in PDF report test: {e}")
        return False

    print("\n=== ALL VERIFICATION CHECKS PASSED SUCCESSFULLY ===")
    return True

if __name__ == '__main__':
    success = run_verification()
    exit(0 if success else 1)
