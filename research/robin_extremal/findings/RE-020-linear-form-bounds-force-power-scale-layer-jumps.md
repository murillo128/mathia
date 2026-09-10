# RE-020 — linear-form bounds force power-scale jumps between bounded CA event-ladder collisions

**Status:** `LITERATURE+DERIVED + BAKER-AMPLIFIED-LAYER-JUMPS + POWER-SAVING-HOST-SPARSITY + DIOPHANTINE-REDUCTION + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`. `RE-018` reduces every infinite family of regular self-tangent CA local Robin peaks in a fixed ordinary-prime envelope to repeated bounded additive near-collisions between two fixed distinct prime-power event ladders. `RE-019` then uses only integrality to show that successive such collisions require logarithmically growing jumps in at least one layer index. A classical lower bound for a nonzero linear form in two logarithms amplifies that spacing from logarithmic to a positive power of the current layer depth.

For a prime `r` and layer `j>=1`, retain the CA event notation

\[
S_{r,j}=r+r^2+\cdots+r^j,\qquad
\lambda_{r,j}=\log(1+S_{r,j}^{-1}),
\]

\[
A_{r,j}:=\frac{\log r}{\lambda_{r,j}},
\qquad
\eta_{r,j}\log\eta_{r,j}=A_{r,j}.
\tag{1}
\]

Fix distinct primes `r!=s` and `B>0`. Let

\[
(j_1,k_1),(j_2,k_2),\ldots
\tag{2}
\]

be an infinite sequence with both coordinates strictly increasing and

\[
0<\eta_{s,k_n}-\eta_{r,j_n}\le B,
\qquad
\eta_{r,j_n}\to\infty.
\tag{3}
\]

Put

\[
a_n:=j_{n+1}-j_n,\qquad
b_n:=k_{n+1}-k_n,\qquad
m_n:=\max(a_n,b_n).
\tag{4}
\]

Then there are effectively computable constants `c_{r,s,B}>0` and `delta_{r,s}>0` such that, for all sufficiently large `n`,

\[
\boxed{
m_n\ge c_{r,s,B}\,j_n^{\delta_{r,s}}.
}
\tag{5}
\]

The exponent need not be optimized. It is enough that it is strictly positive and depends only on the fixed pair of prime bases.

Consequently, if `C_{r,s,B}(Z)` counts pairs satisfying (3) with `eta_(r,j)<=Z`, then

\[
\boxed{
C_{r,s,B}(Z)
=
O_{r,s,B}\!\left(
(\log Z)^{1/(1+\delta_{r,s})}
\right).
}
\tag{6}
\]

Transferring this to the finite family of fixed base pairs supplied by `RE-018`, for every fixed `G>0` there is an effectively computable `kappa_G>0` such that the number `N_G(Z)` of sufficiently large regular self-tangent CA local peaks with `X=\log C<=Z` and ordinary-prime envelope gap `g(C)<=G` satisfies

\[
\boxed{
N_G(Z)=O_G\!\left((\log Z)^{1-\kappa_G}\right).
}
\tag{7}
\]

This is a genuine power saving over the `O_G(\log Z/\log\log Z)` host bound of `RE-019`. It still permits infinitely many candidate peaks and therefore does not prove Robin's inequality.

## 1. Two successive bounded collisions expose a homogeneous logarithmic increment

`RE-019` proves, for every fixed prime `r`,

\[
\eta_{r,j}
=
\frac{r^{j+1}}{(r-1)j}
\left(
1+O_r\!\left(\frac{\log j}{j}\right)
\right).
\tag{8}
\]

It also shows that bounded collisions synchronize the two depths:

\[
k_n
=
\frac{\log r}{\log s}\,j_n
+
O_{r,s,B}(\log j_n),
\tag{9}
\]

so in particular `k_n\asymp_{r,s} j_n`.

Suppose first that

\[
a_n\le \frac{j_n}{2},
\qquad
b_n\le \frac{k_n}{2}.
\tag{10}
\]

The asymptotic (8), used at `j` and `j+a`, is then uniform enough to retain the slowly varying rational factor:

\[
\frac{\eta_{r,j+a}}{\eta_{r,j}}
=
r^a\frac{j}{j+a}
\left(
1+O_r\!\left(\frac{\log j}{j}\right)
\right),
\tag{11}
\]

and similarly

\[
\frac{\eta_{s,k+b}}{\eta_{s,k}}
=
s^b\frac{k}{k+b}
\left(
1+O_s\!\left(\frac{\log k}{k}\right)
\right).
\tag{12}
\]

Write

\[
x_n:=\eta_{r,j_n},
\qquad
y_n:=\eta_{s,k_n}.
\]

From (3),

\[
\frac{y_n}{x_n}=1+O_B(x_n^{-1}),
\]

and therefore

\[
\frac{x_{n+1}/x_n}{y_{n+1}/y_n}
=
\frac{x_{n+1}}{y_{n+1}}\frac{y_n}{x_n}
=
1+O_B(x_n^{-1}).
\tag{13}
\]

Combining (9), (11)--(13) gives

\[
\frac{r^{a_n}}{s^{b_n}}
\frac{j_n}{j_n+a_n}
\frac{k_n+b_n}{k_n}
=
1+O_{r,s,B}\!\left(\frac{\log j_n}{j_n}\right).
\tag{14}
\]

Taking logarithms produces the key cancellation of the fixed ladder normalizations:

\[
\boxed{
\Lambda_n
:=
a_n\log r-b_n\log s
=
\log\!\left(1+\frac{a_n}{j_n}\right)
-
\log\!\left(1+\frac{b_n}{k_n}\right)
+
O_{r,s,B}\!\left(\frac{\log j_n}{j_n}\right).
}
\tag{15}
\]

Hence

\[
\boxed{
|\Lambda_n|
\ll_{r,s,B}
\frac{m_n+\log j_n}{j_n}.
}
\tag{16}
\]

If either inequality in (10) fails, then (9) already gives `m_n\gg_{r,s}j_n`, which is stronger than (5) for any exponent below one. Thus only the moderate-increment regime (10) needs Diophantine input.

The distinction from a single CA event collision is essential. A single comparison of `eta_(r,j)` and `eta_(s,k)` contains fixed normalization terms involving the ladder constants and the slowly varying `j,k` factors. Passing to **two successive collisions** cancels those fixed normalizations and exposes the homogeneous form `a log r-b log s`.

## 2. Matveev's theorem turns the homogeneous increment into a power jump

Because `r` and `s` are distinct primes, they are multiplicatively independent. Thus

\[
\Lambda=a\log r-b\log s
\]

is nonzero for every pair of positive integers `a,b`.

A standard fixed-number consequence of Matveev's explicit lower bound for linear forms in logarithms of algebraic numbers is that there exist effectively computable constants

\[
c_0=c_0(r,s)>0,
\qquad
C_0=C_0(r,s)>0
\]

such that, with `m=max(a,b)>=2`,

\[
\boxed{
|a\log r-b\log s|
\ge c_0\,m^{-C_0}.
}
\tag{17}
\]

Only this qualitative polynomial lower bound is used; no attempt is made to optimize `C_0`.

Apply (17) to `a=a_n`, `b=b_n`. First, (16)--(17) rule out `m_n<=\log j_n` for all sufficiently large `n`, because that would give simultaneously

\[
|\Lambda_n|
\gg_{r,s}(\log j_n)^{-C_0}
\]

and

\[
|\Lambda_n|
\ll_{r,s,B}\frac{\log j_n}{j_n},
\]

which are incompatible as `j_n\to\infty`. Hence eventually `m_n>\log j_n`, and (16) simplifies to

\[
|\Lambda_n|
\ll_{r,s,B}\frac{m_n}{j_n}.
\tag{18}
\]

Combining (17) and (18),

\[
m_n^{C_0+1}\gg_{r,s,B} j_n.
\tag{19}
\]

Thus (5) holds with, for example,

\[
\boxed{
\delta_{r,s}:=\frac{1}{C_0(r,s)+1}>0.
}
\tag{20}
\]

This argument uses the logarithmic-form theorem at the **increment level**, not as a direct lower bound for one Lambert-`W` event gap. It therefore does not resolve the exact simultaneous-jump problem discussed by Alaoglu--Erdos and does not contradict the prior-art warning in `RE-018`.

## 3. Power layer jumps give a power saving in the collision count

Let

\[
M=C_{r,s,B}(Z)
\]

and order the collisions by their left coordinate. `RE-019` proves

\[
j_M+k_M=O_{r,s,B}(\log Z).
\tag{21}
\]

After discarding finitely many initial collisions, (5) applies. Since the positive integer sequence `j_n` is strictly increasing, `j_n>=n` up to a harmless index shift. Therefore

\[
a_n+b_n
\ge m_n
\gg_{r,s,B}
j_n^{\delta_{r,s}}
\gg_{r,s,B}
n^{\delta_{r,s}}.
\tag{22}
\]

Summing (22) for `n<M` gives

\[
j_M+k_M
\gg_{r,s,B}
M^{1+\delta_{r,s}}.
\tag{23}
\]

Together with (21),

\[
M^{1+\delta_{r,s}}
\ll_{r,s,B}\log Z,
\]

which proves (6).

The saving is structurally different from the `log log` factor in `RE-019`. Integrality alone says that near-collisions cannot recur after two simultaneously small exponential increments. The logarithmic-form lower bound says the increment pair itself cannot approximate the required ratio closely enough unless at least one layer jump grows like a fixed positive power of the current depth.

## 4. Transfer to fixed ordinary-prime envelopes

Fix `G>0`. `RE-018` proves that every prime factor appearing at either boundary of a sufficiently large regular self-tangent CA local peak with `g(C)<=G` lies in the finite set

\[
\mathcal P_G
=
\{r\ {\rm prime}:r<e^{2G+3}\},
\tag{24}
\]

and the two adjacent transition coordinates are at distance below `G+1`. `RE-019` then partitions the peak hosts into finitely many ordered pairs of distinct bases `(r,s)` from `mathcal P_G`, with both selected layer indices increasing.

For each ordered pair use (6) with `B=G+1`. Since there are only finitely many pairs, define

\[
\delta_G
:=
\min_{\substack{r,s\in\mathcal P_G\\r\ne s}}
\delta_{r,s}>0
\]

over the nonempty pair classes that can occur, and set

\[
\kappa_G
:=
\frac{\delta_G}{1+\delta_G}>0.
\tag{25}
\]

Summing the pairwise bounds gives

\[
N_G(Z)
=
O_G\!\left(
(\log Z)^{1/(1+\delta_G)}
\right)
=
O_G\!\left(
(\log Z)^{1-\kappa_G}
\right),
\]

which is (7). The constants and the positive exponent are effective in principle because the logarithmic-form input is explicit, but their numerical values are not claimed to be useful.

## 5. Prior-art and novelty boundary

The Diophantine input is classical. Matveev's explicit theorem gives quantitative lower bounds for nonzero integer linear forms in logarithms of fixed algebraic numbers, and (17) is its standard two-logarithm specialization to the multiplicatively independent rational integers `r` and `s`. No novelty is claimed for Baker's method, for finite irrationality measures of logarithm ratios, or for using linear forms in logarithms to study exponential Diophantine approximation.

The closest CA-specific obstruction remains Alaoglu--Erdos's simultaneous-jump discussion, already anchored in `SOURCES.md`. `RE-018` correctly notes that a **single** bounded CA event collision is not immediately a homogeneous two-logarithm problem because the Lambert-`W` event coordinates carry slowly varying and fixed normalization terms. The new point here is that `RE-019` supplies a second collision. Taking the ratio of the two ladder increments cancels the fixed normalizations and leaves exactly the homogeneous form in (15), where the classical theorem applies.

A targeted search across colossally abundant transition literature and linear-forms-in-logarithms applications did not locate this successive-CA-event-ladder amplification. No blanket novelty claim is made for sparse intersections of lacunary sequences. The durable Mathia delta is the implication

\[
\text{bounded CA event collisions}
\Longrightarrow
\text{power-scale layer jumps}
\Longrightarrow
\text{power-saving bounded-envelope host count}.
\]

`SOURCES.md` records Matveev as the new load-bearing source.

## 6. Boundaries and research consequence

Equation (7) remains a **host-set restriction**, not an exclusion theorem. Every fixed positive power of `log Z` still diverges, so an infinite Robin-counterexample subsequence could in principle survive on the resulting set. The theorem applies only when the ordinary-prime envelope is bounded by a fixed `G`; it provides no uniform exponent when `g(C)` grows with `X`.

The result also does not control the selected mixed prime race on the finite intermediate annulus of `RE-014`--`RE-015`, and it does not show that sparse event-ladder hosts contribute negligibly to that race. It does not prove a lower bound forcing `|\eta_{r,j}-\eta_{s,k}|\to\infty` for one fixed pair of ladders, nor does it solve the Alaoglu--Erdos exact-tie problem. The numerical size of `delta_(r,s)` is not itself significant; only positivity is used.

The bounded-envelope branch is nevertheless narrower than after `RE-019`: any infinite escape must synchronize two fixed deep prime-power ladders at bounded additive event distance while making **power-scale jumps in depth between successive synchronizations**. A genuine closure now requires either a stronger single-collision separation theorem, a way to convert this power sparsity into negligible CA-selected mixed-race mass, or a separate argument showing that hypothetical counterexample peaks cannot escape through growing ordinary-prime envelopes.
