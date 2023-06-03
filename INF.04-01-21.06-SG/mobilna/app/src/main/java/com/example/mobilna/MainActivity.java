package com.example.mobilna;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        EditText etEmail = findViewById(R.id.etEmail);
        EditText etPassword = findViewById(R.id.etPassword);
        EditText etPasswordRepeat = findViewById(R.id.etPasswordRepeat);

        TextView tvAlert = findViewById(R.id.tvAlert);

        Button btnSubmit = findViewById(R.id.btnSubmit);
        btnSubmit.setOnClickListener(v -> {
            String email = etEmail.getText().toString();
            String password = etPassword.getText().toString();
            String passwordRepeat = etPasswordRepeat.getText().toString();

            if (!email.contains("@")) {
                tvAlert.setText(R.string.email_invalid);
                return;
            }

            if (!password.equals(passwordRepeat)) {
                tvAlert.setText(R.string.passwords_differs);
                return;
            }

            StringBuilder sb = new StringBuilder();
            sb.append("Witaj ").append(email);
            tvAlert.setText(sb.toString());
        });
    }
}