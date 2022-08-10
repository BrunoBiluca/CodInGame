#include <algorithm>
#include <iostream>
#include <math.h>
#include <string>
#include <vector>

using namespace std;

class Vector2 {
public:
  string name;
  float x;
  float y;

  Vector2() {
    this->x = 0;
    this->y = 0;
  }

  Vector2(string name, float x, float y) {
    this->name = name;
    this->x = x;
    this->y = y;
  }

  string toString() {
    return name + " ( " + to_string(x) + " , " + to_string(y) + " ) ";
  };

  float magnitude() { return sqrt(pow(this->x, 2) + pow(this->y, 2)); }

  Vector2 normalize() {
    auto mag = this->magnitude();
    return Vector2(this->name, this->x / mag, this->y / mag);
  }
};

class FloatExpr {
public:
  static bool nearEqual(float a, float b, float delta) {
    return b - delta <= a && a <= b + delta;
  }
};

class Vector2Expr {
public:
  static float dotProduct(Vector2 a, Vector2 b) {
    return a.x * b.x + a.y * b.y;
  }
};

class IQuadrilateral {
public:
  Vector2 A;
  Vector2 B;
  Vector2 C;
  Vector2 D;
  Vector2 AB;
  Vector2 BC;
  Vector2 CD;
  Vector2 DA;
};

class IQuadrilateralTypeEvaluator {
public:
  virtual string getType(IQuadrilateral q) = 0;
};

class QuadrilateralTypeEvaluator : public IQuadrilateralTypeEvaluator {

private:
  bool areSidesParallel(Vector2 a, Vector2 b) {
    auto result = Vector2Expr::dotProduct(a.normalize(), b.normalize());
    return FloatExpr::nearEqual(result, 1.0f, 0.000001f) ||
           FloatExpr::nearEqual(result, -1.0f, 0.000001f);
  }

  bool areSidesPerpendicular(Vector2 a, Vector2 b) {
    auto result = Vector2Expr::dotProduct(a.normalize(), b.normalize());
    return FloatExpr::nearEqual(result, 0.0f, 0.000001f);
  }

  bool areSidesEqual(IQuadrilateral q) {
    vector<Vector2> sides;
    sides.push_back(q.AB);
    sides.push_back(q.BC);
    sides.push_back(q.CD);
    sides.push_back(q.DA);

    auto magRef = sides.front().magnitude();
    for (auto side : sides) {
      if (side.magnitude() != magRef)
        return false;
    }
    return true;
  }

  bool areAllSidesPerpendicular(IQuadrilateral q) {
    return areSidesPerpendicular(q.AB, q.BC) &&
           areSidesPerpendicular(q.BC, q.CD) &&
           areSidesPerpendicular(q.CD, q.DA) &&
           areSidesPerpendicular(q.DA, q.AB);
  }

public:
  QuadrilateralTypeEvaluator() {}
  string getType(IQuadrilateral q) {
    if (areSidesEqual(q) && areAllSidesPerpendicular(q)) {
      return "square";
    }

    if (areSidesEqual(q)) {
      return "rhombus";
    }

    if (areAllSidesPerpendicular(q)) {
      return "rectangle";
    }

    if (areSidesParallel(q.AB, q.CD) && areSidesParallel(q.BC, q.DA)) {
      return "parallelogram";
    }

    return "quadrilateral";
  }
};

class Quadrilateral : public IQuadrilateral {
private:
  string type;

  Vector2 createVector(const Vector2 &a, const Vector2 &b) {
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

    this->type = QuadrilateralTypeEvaluator().getType(*this);
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
    quadrilaterals.push_back(Quadrilateral(A, B, C, D));
  }

  for (auto &quadrilateral : quadrilaterals) {
    auto sides = quadrilateral.getSidesNames();
    auto type = quadrilateral.getTypeString();
    cout << sides << " is a " << type << "." << endl;
  }
}