import io.kotlintest.matchers.shouldBe
import io.kotlintest.properties.*
import io.kotlintest.specs.StringSpec

class MyTests : StringSpec() {
    init {
        "Test1: Java Navy Sinks Kotlin Navy's Smyshlenyy with an odd number (1)" {
            OOBattleship(JAVA_NAVY, 1) shouldBe KOTLIN_NAVY
        }
        "Test2: Kotlin Navy Sinks Groovy Navy's HMS Shag-at-Sea with a Fibonacci series number (5)" {
            OOBattleship(KOTLIN_NAVY, 5) shouldBe GROOVY_NAVY
        }
        "Test3: Java Navy Does Not Sink Kotlin Navy's ship with an even number (2)" {
            OOBattleship(JAVA_NAVY, 2) shouldBe JAVA_NAVY
        }
        "Test4: Kotlin Navy Does Not Sink Groovy Navy's ship with a Fibonacci series number (4)" {
            OOBattleship(KOTLIN_NAVY, 4) shouldBe KOTLIN_NAVY
        }
        "Test5: Groovy Navy Sinks Java Navy's HNLMS Java with an even number (10)" {
            OOBattleship(GROOVY_NAVY, 10) shouldBe JAVA_NAVY
        }
        "Test6: Java Navy Sinks Kotlin Navy's Smyshlenyy with an odd number (5)" {
            OOBattleship(JAVA_NAVY, 5) shouldBe KOTLIN_NAVY
        }
        "Test7: Groovy Navy Sinks Java Navy's HNLMS Java with an even number (8)" {
            OOBattleship(GROOVY_NAVY, 8) shouldBe JAVA_NAVY
        }
        "Test8: Kotlin Navy Sinks Groovy Navy's HMS Shag-at-Sea with a Fibonacci series number (8)" {
            OOBattleship(KOTLIN_NAVY, 8) shouldBe GROOVY_NAVY
        }
        "Test9: Groovy Navy Sinks Java Navy's HNLMS Java with an even number (200)" {
            OOBattleship(GROOVY_NAVY, 200) shouldBe JAVA_NAVY
        }
        "Test10: Groovy Navy Does Not Sink Java Navy's HNLMS Java with an even number (201)" {
            OOBattleship(GROOVY_NAVY, 201) shouldBe GROOVY_NAVY
        }
    }
}

class DDDExample : StringSpec() {
    init {
        "all OOBattleship test cases" {
            val myTable = table(
                    headers("navyTest", "guessTest", "result"),
                    row(JAVA_NAVY, 1, KOTLIN_NAVY),
                    row(KOTLIN_NAVY, 5, GROOVY_NAVY),
                    row(JAVA_NAVY, 2, JAVA_NAVY),
                    row(KOTLIN_NAVY, 4, KOTLIN_NAVY),
                    row(GROOVY_NAVY, 10, JAVA_NAVY),
                    row(JAVA_NAVY, 5, KOTLIN_NAVY),
                    row(GROOVY_NAVY, 8, JAVA_NAVY),
                    row(KOTLIN_NAVY, 8, GROOVY_NAVY),
                    row(GROOVY_NAVY, 200, JAVA_NAVY),
                    row(GROOVY_NAVY, 201, GROOVY_NAVY)
            )
            forAll(myTable) { navyTest, guessTest, result ->
                OOBattleship(navyTest, guessTest) shouldBe result
            }
        }
    }
}

