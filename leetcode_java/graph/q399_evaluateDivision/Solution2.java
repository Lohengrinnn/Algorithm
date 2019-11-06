package graph.q399_evaluateDivision;

import java.util.*;

public class Solution2 {
    private HashMap<String, HashMap<String, Double>> buildGraph(List<List<String>> equations, double[] values) {
        HashMap<String, HashMap<String, Double>> graph = new HashMap<>();
        for (int i = 0; i < equations.size(); i++) {
            List<String> equation = equations.get(i);
            double value = values[i];
            String v0 = equation.get(0);
            String v1 = equation.get(1);
            if (!graph.containsKey(v0))
                graph.put(v0, new HashMap<String, Double>());
            graph.get(v0).put(v1, value);

            if (!graph.containsKey(v1))
                graph.put(v1, new HashMap<String, Double>());
            graph.get(v1).put(v0, 1d / value);
        }
        return graph;
    }

    private double findPath(HashMap<String, HashMap<String, Double>> graph, List<String> query) {
        String v0 = query.get(0);
        String v1 = query.get(1);
        List<String> visited = new ArrayList<>();
        Queue<String> waitedString = new LinkedList<>();
        Queue<Double> waitedQuo = new LinkedList<>();
        waitedString.offer(v0);
        waitedQuo.offer(1d);
        while (!waitedString.isEmpty()) {
            String s = waitedString.poll();
            double quo = waitedQuo.poll();
            if (!graph.containsKey(s))
                continue;
            visited.add(s);
            if (s.equals(v1)) {
                return quo;
            }
            for (Map.Entry<String, Double> edge: graph.get(s).entrySet()) {
                String v = edge.getKey();
                double value = edge.getValue();
                double v0ToV = quo * value;
                graph.get(v0).put(v, v0ToV);
                if (!visited.contains(v)) {
                    waitedString.offer(v);
                    waitedQuo.offer(v0ToV);
                }
            }
        }
        return -1;
    }

    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        HashMap<String, HashMap<String, Double>> graph = buildGraph(equations, values);
        System.out.println(graph);
        double[] res = new double[queries.size()];
        for (int i = 0; i < queries.size(); i++) {
            List<String> query = queries.get(i);
            res[i] = findPath(graph, query);
        }
        return res;
    }

    public static void main(String[] args) {
        List<List<String>> equations = new ArrayList<List<String>>();
        equations.add(new ArrayList<String>(Arrays.asList(new String[]{"a", "b"})));
        equations.add(new ArrayList<String>(Arrays.asList(new String[]{"b", "c"})));
        double[] values = {2.0, 3.0};
        List<List<String>> queries = new ArrayList<List<String>>();
        queries.add(new ArrayList<String>(Arrays.asList(new String[]{"a", "c"})));
        queries.add(new ArrayList<String>(Arrays.asList(new String[]{"b", "a"})));
        queries.add(new ArrayList<String>(Arrays.asList(new String[]{"a", "e"})));
        queries.add(new ArrayList<String>(Arrays.asList(new String[]{"a", "a"})));
        queries.add(new ArrayList<String>(Arrays.asList(new String[]{"x", "x"})));
        double[] res = (new Solution2().calcEquation(equations, values, queries));
        for (double d: res)
            System.out.println(d);
    }
}
