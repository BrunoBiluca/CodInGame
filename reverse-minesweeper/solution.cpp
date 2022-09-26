#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

// To debug: cerr << "Debug messages..." << endl;

std::string Concat(const std::vector<std::string> &elements,
                   const std::string &separator) {
  if (elements.empty()) {
    return "";
  }

  std::stringstream ss;
  auto it = elements.cbegin();
  while (true) {
    ss << *it++;

    if (it == elements.cend())
      return ss.str();

    ss << separator;
  }
}

class Position {
public:
  int x;
  int y;
  Position(int x, int y) {
    this->x = x;
    this->y = y;
  }
};

class ICell {
public:
  virtual bool IsMine() = 0;
  virtual int GetIndex() = 0;
};

class IMineGrid {
public:
  virtual void SetIsMine(int x, int y) = 0;
  virtual int GetMinesBordering(ICell *cell) = 0;
};

class Cell : ICell {
private:
  int index;
  IMineGrid *grid;

  bool isMine;

public:
  Cell() {}
  Cell(int index, IMineGrid *grid) {
    this->isMine = false;
    this->index = index;
    this->grid = grid;
  }
  bool IsMine() { return this->isMine; }
  void SetIsMine() { this->isMine = true; }
  int GetIndex() { return this->index; }
  int MinesBorderingCount() { return grid->GetMinesBordering(this); }
};

class Grid : public IMineGrid {
private:
  int width;
  int height;
  vector<Cell> cells;
  int GetIndex(int x, int y) { return y * width + x; }

public:
  Grid(int width, int height) {
    this->width = width;
    this->height = height;
    cells = vector<Cell>(width * height);
    for (int y = 0; y < height; y++) {
      for (int x = 0; x < width; x++) {
        cells[this->GetIndex(x, y)] = Cell(this->GetIndex(x, y), this);
      }
    }
  }

  void SetIsMine(int x, int y) { cells[this->GetIndex(x, y)].SetIsMine(); }

  Cell GetCell(int x, int y) { return cells[this->GetIndex(x, y)]; }

  int GetWidth() { return this->width; }

  int GetHeight() { return this->height; }

  int GetMinesBordering(ICell *cell) {
    auto amount = 0;
    for (auto neighbourPos : GetValidNeighbors(cell)) {
      if (neighbourPos.x < 0 || neighbourPos.y < 0 || neighbourPos.x >= width ||
          neighbourPos.y >= height)
        continue;

      if (cells[GetIndex(neighbourPos.x, neighbourPos.y)].IsMine())
        amount++;
    }
    return amount;
  }

  vector<Position> GetValidNeighbors(ICell *cell) {
    auto cX = cell->GetIndex() % width;
    auto cY = cell->GetIndex() / width;

    auto neighborsPositions = vector<Position>{
        Position(cX - 1, cY - 1), Position(cX, cY - 1),
        Position(cX + 1, cY - 1),

        Position(cX - 1, cY),     Position(cX + 1, cY),

        Position(cX - 1, cY + 1), Position(cX, cY + 1),
        Position(cX + 1, cY + 1),
    };

    auto validNeighbors = vector<Position>();

    for (auto neighbourPos : neighborsPositions) {
      if (neighbourPos.x < 0 || neighbourPos.y < 0 || neighbourPos.x >= width ||
          neighbourPos.y >= height)
        continue;

      validNeighbors.push_back(neighbourPos);
    }
    return validNeighbors;
  }
};

class MineResultDisplayHandler {

private:
  char emptyCell() { return '.'; }
  char minesBorderingCell(int amount) {
    std::string s = std::to_string(amount);
    return *s.c_str();
  }

  char evaluateCell(Cell c) {
    if (c.IsMine())
      return emptyCell();

    auto minesNear = c.MinesBorderingCount();

    if (minesNear == 0)
      return emptyCell();

    return minesBorderingCell(minesNear);
  }

public:
  string Display(Grid grid) {
    auto display = vector<string>(grid.GetHeight(), "");
    auto counter = 0;

    for (int y = 0; y < grid.GetHeight(); y++) {
      for (int x = 0; x < grid.GetWidth(); x++) {
        display[y] += evaluateCell(grid.GetCell(x, y));
      }
    }

    return Concat(display, "\n");
  }
};

int main() {
  int w;
  cin >> w;
  cin.ignore();
  int h;
  cin >> h;
  cin.ignore();

  auto grid = Grid(w, h);

  for (int i = 0; i < h; i++) {
    string line;
    getline(cin, line);

    for (int j = 0; j < line.size(); j++) {
      if (line[j] == 'x')
        grid.SetIsMine(j, i);
    }
  }

  cout << MineResultDisplayHandler().Display(grid) << endl;
}