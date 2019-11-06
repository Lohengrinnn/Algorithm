package graph.q399_evaluateDivision;

import java.util.*;

class Solution {
    private int find(String s, List<HashMap<String, Double>> disjoint_set) {
        for (int i = 0; i < disjoint_set.size(); i++) {
            HashMap<String, Double> set = disjoint_set.get(i);
            if (set.containsKey(s))
                return i;
        }
        return -1;
    }

    private void union(List<HashMap<String, Double>> disjoint_set, int x, int y, List<String> equation, Double value) {
        HashMap<String, Double> child = disjoint_set.remove(y);
        HashMap<String, Double> parent = disjoint_set.get(x);
        double pdc = value * parent.get(equation.get(0)) / child.get(equation.get(1));
        for (Map.Entry<String, Double> quo: child.entrySet()) {
            parent.put(quo.getKey(), quo.getValue() * pdc);
        }

    }
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        List<HashMap<String, Double>> disjoint_set = new ArrayList<>();
        double[] res = new double[queries.size()];
        for (int i = 0; i < equations.size(); i++) {
            List<String> equation = equations.get(i);
            double value = values[i];
            int x = find(equation.get(0), disjoint_set);
            int y = find(equation.get(1), disjoint_set);
            if (x == -1 && y == -1) {
                HashMap<String, Double> new_set = new HashMap<String, Double>();
                new_set.put(equation.get(0), 1d);
                new_set.put(equation.get(1), value);
                disjoint_set.add(new_set);
            } else if (y == -1) {
                disjoint_set.get(x).put(equation.get(1), disjoint_set.get(x).get(equation.get(0)) * value);
            } else if (x == -1) {
                disjoint_set.get(y).put(equation.get(0), disjoint_set.get(y).get(equation.get(1)) / value);
            } else {
                union(disjoint_set, x, y, equation, value);
            }
            System.out.println(disjoint_set);
        }
        int i = 0;
        for (List<String> query: queries) {
            int x = find(query.get(0), disjoint_set);
            int y = find(query.get(1), disjoint_set);
            if (x != y || x == -1 || y == -1) {
                res[i] = -1d;
            } else {
                System.out.printf("x:%d(%s, %f), y:%d(%s, %f)",
                        x, query.get(0), disjoint_set.get(x).get(query.get(0)),
                        y, query.get(1), disjoint_set.get(y).get(query.get(1)));
                res[i] = disjoint_set.get(y).get(query.get(1)) / disjoint_set.get(x).get(query.get(0));
            }
            i++;
        }
        return res;
    }
    /*
     * [["a","e"],["b","e"]]
     * [4.0,3.0]
     * [["a","b"],["e","e"],["x","x"]]
     * */
    public static void main(String[] args) {
        List<List<String>> equations = new ArrayList<List<String>>();
        equations.add(new ArrayList<String>(Arrays.asList(new String[]{"a", "e"})));
        equations.add(new ArrayList<String>(Arrays.asList(new String[]{"b", "e"})));
        double[] values = {4.0, 3.0};
        List<List<String>> queries = new ArrayList<List<String>>();
        queries.add(new ArrayList<String>(Arrays.asList(new String[]{"a", "c"})));
        queries.add(new ArrayList<String>(Arrays.asList(new String[]{"b", "a"})));
        queries.add(new ArrayList<String>(Arrays.asList(new String[]{"e", "e"})));
        queries.add(new ArrayList<String>(Arrays.asList(new String[]{"a", "a"})));
        queries.add(new ArrayList<String>(Arrays.asList(new String[]{"x", "x"})));
        double[] res = (new Solution().calcEquation(equations, values, queries));
        for (double d: res)
            System.out.println(d);
    }
}