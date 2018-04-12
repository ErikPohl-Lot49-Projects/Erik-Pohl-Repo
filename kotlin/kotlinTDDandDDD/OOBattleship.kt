var KOTLIN_NAVY = "Kotlin Navy"
var JAVA_NAVY = "Java Navy"
var GROOVY_NAVY = "Groovy Navy"


fun isFibonacci(testNum : Int) : Int {
    var min = 0
    var max = 1
    var newmax = 0
    while (min <= testNum) {
             if (min == testNum || max == testNum) {
                return 1 }
            else {
                newmax = min + max
                min = max
                max = newmax
            }
        }
        return 0
}

fun OOBattleship(navyName: String, Guess: Int) : String {
    if (navyName == JAVA_NAVY && (Guess % 2) == 1) { // oh, you mean odd! and the current state is Java Navy's turn!!
        return KOTLIN_NAVY
    }
    if (navyName == KOTLIN_NAVY && isFibonacci(Guess)==1) { // fibonacci and current state is Kotlin Navy's turn!!
        return GROOVY_NAVY
    }
    if (navyName == GROOVY_NAVY && Guess % 2 == 0) { // all even numbers!
        return JAVA_NAVY
    }
    return navyName
}

fun main(args : Array<String>) {
    println(OOBattleship(JAVA_NAVY, 3))
}