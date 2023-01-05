#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

template <typename T> bool hasElement(vector<T> vec, T elem) {
  return std::find(vec.begin(), vec.end(), elem) != vec.end();
}

class Island {
public:
  vector<int> land;
  vector<int> coast;
  void add_coast(int posIndex) {
    if (!hasElement(coast, posIndex))
      coast.push_back(posIndex);
  }
  void add_land(int posIndex) {
    if (!hasElement(land, posIndex))
      land.push_back(posIndex);
  }
  int get_coast_size(){
    return coast.size();
  }
};

class IslandResult {
public:
  int islandIndex = -1;
  int coastSize = -1;
};

int getX(int index, int n) { return index / n; }
int getY(int index, int n) { return index % n; }

int tryGetLeft(int index, int n, int &left) {
  left = index - 1;
  return left >= 0;
}

int tryGetUp(int y, int n, int &up) {
  up = y - n;
  return up >= 0;
}

int tryGetRight(int index, int n, int &right) {
  right = index + 1;
  return 0 < getY(right, n) && getY(right, n) < n;
}

int tryGetDown(int index, int n, int &down) {
  down = index + n;
  return 0 < getX(down, n) && getX(down, n) < n;
}

Island createNewIsland(vector<char> grid, int gridDim, int index) {
  Island newIsland;

  vector<int> notExplored;
  notExplored.push_back(index);
  newIsland.add_land(index);

  while (!notExplored.empty()) {
    auto exploringPos = notExplored.back();
    notExplored.pop_back();

    vector<int> neighbours;
    int left, up, right, down;
    if (tryGetLeft(exploringPos, gridDim, left))
      neighbours.push_back(left);
    if (tryGetUp(exploringPos, gridDim, up))
      neighbours.push_back(up);
    if (tryGetRight(exploringPos, gridDim, right))
      neighbours.push_back(right);
    if (tryGetDown(exploringPos, gridDim, down))
      neighbours.push_back(down);

    for (auto neighbour : neighbours) {
      if (hasElement(newIsland.land, neighbour))
        continue;

      char pos = grid[neighbour];
      if (grid[neighbour] == '#') {
        notExplored.push_back(neighbour);
        newIsland.add_land(neighbour);
      } else
        newIsland.add_coast(neighbour);
    }
  }
  return newIsland;
}

bool hasLandOnSomeIsland(int pos, vector<Island> islands) {
  for (auto island : islands)
    if (hasElement(island.land, pos))
      return true;

  return false;
}

int main() {
  int n;
  cin >> n;
  cin.ignore();

  vector<char> grid;
  for (int i = 0; i < n; i++) {
    string row;
    getline(cin, row);
    for (int j = 0; j < n; j++) {
      grid.push_back(row[j]);
    }
  }

  IslandResult longestCoast;
  vector<Island> islands;
  for (int i = 0; i < n * n; i++) {
    auto currPos = grid[i];
    if (currPos != '#')
      continue;
    if (hasLandOnSomeIsland(i, islands))
      continue;

    cerr << "Creating island => " << i << endl;
    auto newIsland = createNewIsland(grid, n, i);
    islands.push_back(newIsland);

    if (newIsland.get_coast_size() > longestCoast.coastSize) {
      cerr << "Changing longest island" << endl;
      longestCoast.islandIndex = islands.size();
      longestCoast.coastSize = newIsland.coast.size();
    }
  }

  cout << longestCoast.islandIndex << " " << longestCoast.coastSize << endl;
}