#include <algorithm>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

vector<string> split(string text, char separator) {
  string str;
  stringstream ss(text);
  vector<string> result;
  while (getline(ss, str, separator)) {
    result.push_back(str);
  }
  return result;
}

float convertMilisecondsToHours(long long value) {
  return ((float)value) / ((float)(60 * 60 * 1000));
}

float evaluateVelocityKmH(float aPos, long long aTime, float bPos,
                          long long bTime) {
  auto distance = aPos - bPos;
  auto diffTime = convertMilisecondsToHours(aTime - bTime);
  return distance / diffTime;
}

class ScannedPlate {
private:
  string plate;
  string radarName;
  long long scannedAt;
  int kilometer;

public:
  ScannedPlate(string plate, string radarName, long long scannedAt) {
    this->plate = plate;
    this->radarName = radarName;
    this->scannedAt = scannedAt;

    auto radarKilometer = split(radarName, '-').back();
    this->kilometer = stoi(radarKilometer);
  }
  string getPlate() { return this->plate; }
  string getRadarName() { return this->radarName; }
  long long getScannedAt() { return this->scannedAt; }
  int getKilometer() { return this->kilometer; }
};

bool scannedPlateCompare(ScannedPlate a, ScannedPlate b) {
  return a.getScannedAt() < b.getScannedAt();
}

class CarVelocity {
public:
  string plate;
  int velocity;
  CarVelocity(string plate, int velocity) {
    this->plate = plate;
    this->velocity = velocity;
  }
};

class CarScannedHistory {
private:
  map<string, vector<ScannedPlate>> scannedHistory = {};

public:
  void add(ScannedPlate scannedPlate) {
    auto plate = scannedPlate.getPlate();
    if (scannedHistory.count(plate) == 0) {
      scannedHistory.insert({plate, vector<ScannedPlate>()});
    }
    auto pos = scannedHistory.find(plate);
    pos->second.push_back(scannedPlate);
  }

  vector<CarVelocity> getCarsOver(int kmh) {
    auto carVelocityReport = vector<CarVelocity>();
    for (auto const &plateHistory : scannedHistory) {
      auto history = plateHistory.second;
      sort(history.begin(), history.end(), scannedPlateCompare);
      for (auto it = 0; it < history.size() - 1; ++it) {
        auto curr = history[it];
        auto next = history[it + 1];

        auto velocity =
            (int)evaluateVelocityKmH(next.getKilometer(), next.getScannedAt(),
                                     curr.getKilometer(), curr.getScannedAt());
        cerr << velocity << endl;
        if (velocity > kmh) {
          carVelocityReport.push_back(
              CarVelocity(plateHistory.first, velocity));
        }
      }
    }
    return carVelocityReport;
  }
};

int main() {
  auto scannedHistory = CarScannedHistory();
  int n;
  cin >> n;
  cin.ignore();
  for (int i = 0; i < n; i++) {
    string plate;
    string radarname;
    long long timestamp;
    cin >> plate >> radarname >> timestamp;
    cin.ignore();
    auto scannedPlate = ScannedPlate(plate, radarname, timestamp);
    scannedHistory.add(scannedPlate);
  }

  for (auto const &carVelocity : scannedHistory.getCarsOver(130)) {
    cout << carVelocity.plate << " " << carVelocity.velocity << endl;
  }
}