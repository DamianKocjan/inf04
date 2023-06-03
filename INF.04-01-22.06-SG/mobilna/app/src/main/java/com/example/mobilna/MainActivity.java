package com.example.mobilna;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    int likes_count = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        TextView tvLikesCount = findViewById(R.id.tvLikesCount);

        Button btnLike = findViewById(R.id.btnLike);
        btnLike.setOnClickListener(v -> {
            likes_count++;
            tvLikesCount.setText(String.format("%d polubień", likes_count));
        });

        Button btnDislike = findViewById(R.id.btnDislike);
        btnDislike.setOnClickListener(v -> {
            likes_count = Math.max(0, likes_count - 1);
            tvLikesCount.setText(String.format("%d polubień", likes_count));
        });
    }
}