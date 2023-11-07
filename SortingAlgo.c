#include <SFML/Graphics.hpp>
#include <iostream>
#include <vector>
#include <random>
#include <chrono>
#include <thread>

const int windowWidth = 800;
const int windowHeight = 600;
const int numBars = 100;
const int barWidth = windowWidth / numBars;

void drawBars(sf::RenderWindow& window, std::vector<int>& arr) {
    window.clear();

    for (int i = 0; i < numBars; i++) {
        sf::RectangleShape bar(sf::Vector2f(barWidth, arr[i]));
        bar.setPosition(i * barWidth, windowHeight - arr[i]);
        bar.setFillColor(sf::Color::Blue);
        window.draw(bar);
    }

    window.display();
}

void bubbleSortVisualizer(sf::RenderWindow& window, std::vector<int>& arr) {
    int n = arr.size();

    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);

                drawBars(window, arr);
                std::this_thread::sleep_for(std::chrono::milliseconds(10)); // Adjust the delay for visualization speed
            }
        }
    }
}

int main() {
    sf::RenderWindow window(sf::VideoMode(windowWidth, windowHeight), "Bubble Sort Visualizer");
    std::vector<int> arr;

    // Generate random data for visualization
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> dist(50, windowHeight - 50);
    for (int i = 0; i < numBars; i++) {
        arr.push_back(dist(gen));
    }

    bubbleSortVisualizer(window, arr);

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed) {
                window.close();
            }
        }
    }

    return 0;
}
