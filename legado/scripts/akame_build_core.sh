#!/bin/bash
echo "🔱 AKAME: Verificando infraestrutura vital..."

verificar_e_criar() {
    FILE=$1
    CONTENT=$2
    DIR=$(dirname "$FILE")
    mkdir -p "$DIR"
    echo "$CONTENT" > "$FILE"
    echo "✅ Akame: Arquivo $FILE forjado com sucesso."
}

# CORPO
XML_BODY='<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent" android:layout_height="match_parent" android:background="#050505">
    <TextView android:id="@+id/status" android:layout_width="wrap_content" android:layout_height="wrap_content"
        android:layout_centerInParent="true" android:text="🔱 AKAME: MOTOR INQUEBRÁVEL ATIVO"
        android:textColor="#FF0000" android:textSize="22sp" android:textStyle="bold" android:gravity="center" />
</RelativeLayout>'

# ALMA
JAVA_SOUL='package com.akame.soberana;
import android.os.Bundle;
import android.speech.tts.TextToSpeech;
import androidx.appcompat.app.AppCompatActivity;
import java.util.Locale;

public class MainActivity extends AppCompatActivity {
    private TextToSpeech tts;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        tts = new TextToSpeech(this, status -> {
            if (status != TextToSpeech.ERROR) {
                tts.setLanguage(new Locale("pt", "BR"));
                tts.speak("Passo 2 concluído. Motores ativos.", TextToSpeech.QUEUE_FLUSH, null, null);
            }
        });
    }
}'

# MAPA
MANIFEST_MAP='<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android" package="com.akame.soberana">
    <application android:allowBackup="true" android:label="Akame Original" android:theme="@style/Theme.AppCompat.NoActionBar">
        <activity android:name=".MainActivity" android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>'

# EXECUTANDO
verificar_e_criar "app/src/main/res/layout/activity_main.xml" "$XML_BODY"
verificar_e_criar "app/src/main/java/com/akame/soberana/MainActivity.java" "$JAVA_SOUL"
verificar_e_criar "app/src/main/AndroidManifest.xml" "$MANIFEST_MAP"
echo "🔱 AKAME: Reconstrução finalizada."
