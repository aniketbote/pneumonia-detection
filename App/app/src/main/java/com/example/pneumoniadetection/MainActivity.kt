package com.example.pneumoniadetection

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        btnShowToast.setOnClickListener {
            Log.i("MainActivity","Button waas clicked")
            Toast.makeText(this, "Button was clicked",Toast.LENGTH_SHORT).show()
        }


    }

}

