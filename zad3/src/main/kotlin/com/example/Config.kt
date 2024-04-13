package com.example

import java.io.FileNotFoundException
import java.util.*

object Config {
    val apiUrl: String

    init {
        val properties = Properties()
        val inputStream = javaClass.classLoader.getResourceAsStream("config.properties")
        if (inputStream != null) {
            properties.load(inputStream)
        } else {
            throw FileNotFoundException("property file 'config.properties' not found in the classpath")
        }

        apiUrl = properties.getProperty("api_url")
    }
}

fun main() {
    println("API URL from properties file: ${Config.apiUrl}")
}
