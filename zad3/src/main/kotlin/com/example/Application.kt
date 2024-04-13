package com.example

import io.ktor.client.*
import io.ktor.client.plugins.contentnegotiation.*
import io.ktor.client.request.*
import io.ktor.client.request.setBody
import io.ktor.client.statement.*
import io.ktor.http.*
import io.ktor.serialization.kotlinx.json.*
import kotlinx.coroutines.*
import kotlinx.serialization.json.Json
import kotlinx.serialization.Serializable

@Serializable
data class Content(val content: String)

fun main() {
    runBlocking {
        while (true) {
            val client = HttpClient() {
                install(ContentNegotiation) {
                    json(Json {
                        prettyPrint = true
                        isLenient = true
                    })
                }
            }

            try {
                println("Enter your message:")
                val userInput = readlnOrNull() ?: ""

                val response: HttpResponse = client.post(Config.apiUrl) {
                    contentType(ContentType.Application.Json)
                    setBody(Content(userInput))
                }

                println("Response from server: ${response.status} ${response.bodyAsText()}")
            } catch (e: Exception) {
                println("An error occurred: ${e.localizedMessage}")
            } finally {
                client.close()
            }
        }
    }
}
