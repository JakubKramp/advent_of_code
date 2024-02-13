package main

import (
    "fmt"
    "io/ioutil"
    "strconv"
    "strings"
    "math"
)

func loadInput() string {
    content, err := ioutil.ReadFile("input.txt")
    if err != nil {
        fmt.Println("Error reading file:", err)
    }
    str := string(content)
    return str
}

func partOne() int {
    str := strings.Split(loadInput(), "\n")
    sum := 0
    for i := 0; i < len(str); i++ {
        min_val := math.MaxInt64
        max_val := math.MinInt64
        numbers := strings.Split(str[i], "\t")
        for j := 0; j<len(numbers); j++{
        num, err := strconv.Atoi(string(numbers[j]))
        if err != nil {
        fmt.Println("Error converting string:", err)
    }
        if num > max_val{
        max_val = num
        }
        if num < min_val{
        min_val = num
        }
        }
        sum += max_val - min_val
}
    return sum
}

func partTwo() int {
    str := strings.Split(loadInput(), "\n")
    sum := 0
    for i := 0; i < len(str); i++ {
        numbers := strings.Split(str[i], "\t")
        for j := 0; j<len(numbers); j++{
        for h := 0; h<len(numbers); h++{
        num, err := strconv.Atoi(string(numbers[j]))
        if err != nil {
        fmt.Println("Error converting string:", err)
    }
        number, err := strconv.Atoi(string(numbers[h]))
        if err != nil {
        fmt.Println("Error converting string:", err)
    }

        if num != number && num % number==0{
        sum += num/number
        }
        }
        }

}
    return sum
}

func main() {
    num := partOne()
    fmt.Println(num)
    number := partTwo()
    fmt.Println(number)
}