#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class IVector2 {
public:
  string name;
  int x;
  int y;
};

class IQuadrilateral {
public:
  IVector2 A;
  IVector2 B;
  IVector2 C;
  IVector2 D;
  IVector2 AB;
  IVector2 BC;
  IVector2 CD;
  IVector2 DA;
  string getSidesNames();
  string getTypeString();
};

class IQuadrilateralTypeEvaluator {
public:
  string getType(IQuadrilateral q);
};

class QuadrilateralTypeEvaluator : public IQuadrilateralTypeEvaluator {

private:
  bool sidesAreParallel(const IVector2 &a, const IVector2 &b) {
    auto dotProduct = a.x * b.x + a.y * b.y;
    cerr << "DP: " << a.name << b.name << " = " << dotProduct << endl;
    return dotProduct == 1 || dotProduct == -1;
  }

public:
  QuadrilateralTypeEvaluator() {}
  string getType(IQuadrilateral q) {
    if (sidesAreParallel(q.AB, q.CD) && sidesAreParallel(q.BC, q.DA)) {
      return "parallelogram";
    }

    return "quadrilateral";
  }
};

class Vector2 : public IVector2 {
public:
  Vector2() {
    this->x = 0;
    this->y = 0;
  }

  Vector2(string name, int x, int y) {
    this->name = name;
    this->x = x;
    this->y = y;
  }
};

class Quadrilateral : public IQuadrilateral {
private:
  string type;

  Vector2 createVector(const IVector2 &a, const IVector2 &b) {
    return Vector2(a.name + b.name, a.x - b.x, a.y - b.y);
  }

public:
  Quadrilateral(Vector2 A, Vector2 B, Vector2 C, Vector2 D) {
    this->A = A;
    this->B = B;
    this->C = C;
    this->D = D;

    this->AB = createVector(this->A, this->B);
    this->BC = createVector(this->B, this->C);
    this->CD = createVector(this->C, this->D);
    this->DA = createVector(this->D, this->A);

    QuadrilateralTypeEvaluator eval;
    this->type = eval.getType(*this);
  }

  string getSidesNames() {
    return this->A.name + this->B.name + this->C.name + this->D.name;
  }

  string getTypeString() { return type; }
};

int main() {
  int n;
  cin >> n;
  cin.ignore();

  vector<Quadrilateral> quadrilaterals;
  for (int i = 0; i < n; i++) {
    string a;
    int x_a;
    int y_a;
    string b;
    int x_b;
    int y_b;
    string c;
    int x_c;
    int y_c;
    string d;
    int x_d;
    int y_d;
    cin >> a >> x_a >> y_a >> b >> x_b >> y_b >> c >> x_c >> y_c >> d >> x_d >>
        y_d;
    cin.ignore();

    Vector2 A(a, x_a, y_a);
    Vector2 B(b, x_b, y_b);
    Vector2 C(c, x_c, y_c);
    Vector2 D(d, x_d, y_d);
    Quadrilateral newQuadrilateral(A, B, C, D);
    quadrilaterals.push_back(newQuadrilateral);
  }

  for (auto &quadrilateral : quadrilaterals) {
    auto sides = quadrilateral.getSidesNames();
    auto type = quadrilateral.getTypeString();
    cout << sides << " is a " << type << "." << endl;
  }
}