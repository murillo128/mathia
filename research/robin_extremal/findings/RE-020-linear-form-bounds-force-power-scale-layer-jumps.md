# RE-020 — linear-form bounds force event-scale power jumps between bounded CA event-ladder collisions

**Status:** `LITERATURE+DERIVED + EXACT-EVENT-PARAMETER-CANCELLATION + EVENT-SCALE-POWER-JUMPS + ITERATED-LOG-HOST-SPARSITY + DIOPHANTINE-REDUCTION + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`. `RE-018` reduces every infinite family of regular self-tangent CA local Robin peaks in a fixed ordinary-prime envelope to repeated bounded additive near-collisions between two fixed distinct prime-power event ladders. `RE-019` shows elementarily that successive such collisions require logarithmically growing layer jumps. The exact CA event parameter removes the slowly varying Lambert-`W` error that appears when one compares event coordinates directly: after taking two successive bounded collisions, the relevant prime-power increment ratio is actually `1+O(1/X)`, where `X` is the event coordinate. A classical lower bound for a nonzero linear form in two logarithms then forces a positive power of **event scale**, equivalently an exponential jump in the current layer depth.

For a prime `r` and layer `j>=1`, retain

\[
S_{r,j}=r+r^2+\cdots+r^j,
\qquad
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
x_n:=\eta_{r,j_n}\longrightarrow\infty.
\tag{3}
\]

Put

\[
a_n:=j_{n+1}-j_n,
\qquad
b_n:=k_{n+1}-k_n,
\qquad
m_n:=\max(a_n,b_n).
\tag{4}
\]

Then there are effectively computable constants `c_(r,s,B)>0` and `delta_(r,s)>0` such that, for all sufficiently large `n`,

\[
\boxed{
m_n\ge c_{r,s,B}\,x_n^{\delta_{r,s}}.
}
\tag{5}
\]

In particular, since `log x_n=j_n log r+O_r(log j_n)`, the jump is exponential in the current ladder depth:

\[
\boxed{
m_n\ge \exp(c'_{r,s}j_n)}
\tag{6}
\]

for a possibly smaller positive constant and all sufficiently large `n`.

More strongly, the next collision coordinate satisfies

\[
\boxed{
\log x_{n+1}\ge c''_{r,s,B}\,x_n^{\delta_{r,s}}.
}
\tag{7}
\]

Thus fixed-base bounded CA event-ladder collisions, if infinite, are super-lacunary. If `C_(r,s,B)(Z)` counts sufficiently large collision pairs with `eta_(r,j)<=Z`, then

\[
\boxed{
C_{r,s,B}(Z)=O_{r,s,B}\!\left(1+\log^*\log Z\right),
}
\tag{8}
\]

where `log^*` is the iterated logarithm, with the harmless additive convention depending only on the fixed starting threshold.

Transferring this to the finite family of fixed base pairs supplied by `RE-018`, for every fixed `G>0`, if `N_G(Z)` counts sufficiently large regular self-tangent CA local peaks with `X=log C<=Z` and ordinary-prime envelope gap `g(C)<=G`, then

\[
\boxed{
N_G(Z)=O_G\!\left(1+\log^*\log Z\right).
}
\tag{9}
\]

This is far thinner than the power-of-`log Z` host bound obtained from a direct Lambert-`W` asymptotic comparison. It still allows an infinite exceptional sequence and therefore does not prove Robin's inequality.

## 1. A bounded event-coordinate collision is an `O(1/x)` collision of the exact CA parameter

Let

\[
f(t)=t\log t.
\]

At the `n`-th collision write

\[
y_n:=\eta_{s,k_n}=x_n+O_B(1).
\]

Because `A_(r,j_n)=f(x_n)` and `A_(s,k_n)=f(y_n)`, the mean-value theorem gives

\[
\frac{A_{s,k_n}}{A_{r,j_n}}
=
\frac{f(y_n)}{f(x_n)}
=
1+O_B(x_n^{-1}).
\tag{10}
\]

The same estimate holds at `n+1`, and `x_(n+1)>=x_n`. Therefore

\[
\frac{A_{r,j_n+a_n}/A_{r,j_n}}
     {A_{s,k_n+b_n}/A_{s,k_n}}
=
\frac{A_{s,k_n}/A_{r,j_n}}
     {A_{s,k_n+b_n}/A_{r,j_n+a_n}}
=
1+O_B(x_n^{-1}).
\tag{11}
\]

This step is where the exact event coordinate matters. Comparing the `eta` ratios themselves introduces the slowly varying `1/j` and Lambert-`W` corrections. Comparing `A=eta log eta` instead preserves the `O(1/x)` accuracy of the bounded additive collision.

## 2. Exact `lambda` ratios cancel the event normalization

From (1),

\[
A_{r,j}=\frac{\log r}{\lambda_{r,j}},
\]

so (11) is exactly

\[
\frac{\lambda_{r,j_n}}{\lambda_{r,j_n+a_n}}
\frac{\lambda_{s,k_n+b_n}}{\lambda_{s,k_n}}
=
1+O_B(x_n^{-1}).
\tag{12}
\]

For every integer `S>=1`,

\[
\frac1{S+1}\le \log(1+S^{-1})\le \frac1S.
\tag{13}
\]

Consequently the event equation gives the useful exact bracket

\[
\boxed{
S_{r,j}
\le
\frac{\eta_{r,j}\log\eta_{r,j}}{\log r}
\le
S_{r,j}+1.
}
\tag{14}
\]

In particular, along (3),

\[
S_{r,j_n}\asymp_{r}x_n\log x_n,
\qquad
S_{s,k_n}\asymp_{s}x_n\log x_n.
\tag{15}
\]

Using

\[
\log(1+S^{-1})
=
S^{-1}\left(1+O(S^{-1})\right)
\tag{16}
\]

inside (12), with the old-layer errors dominating the new-layer errors, yields

\[
\frac{S_{r,j_n+a_n}S_{s,k_n}}
     {S_{r,j_n}S_{s,k_n+b_n}}
=
1+O_B(x_n^{-1}).
\tag{17}
\]

No restriction on the sizes of `a_n,b_n` is needed here.

Now use the exact geometric-sum formula

\[
S_{r,j}=\frac{r(r^j-1)}{r-1}.
\tag{18}
\]

Equation (17) becomes

\[
\frac{r^{a_n}}{s^{b_n}}
V_n
=
1+O_B(x_n^{-1}),
\tag{19}
\]

where

\[
V_n=
\frac{1-r^{-(j_n+a_n)}}{1-r^{-j_n}}
\frac{1-s^{-k_n}}{1-s^{-(k_n+b_n)}}.
\tag{20}
\]

From (15), (18), and the fact that `r,s` are fixed,

\[
r^{-j_n}+s^{-k_n}
=O_{r,s,B}\!\left((x_n\log x_n)^{-1}\right),
\]

hence

\[
V_n=1+O_{r,s,B}\!\left((x_n\log x_n)^{-1}\right).
\tag{21}
\]

Combining (19)--(21) gives the decisive increment-level approximation

\[
\boxed{
\frac{r^{a_n}}{s^{b_n}}
=
1+O_{r,s,B}(x_n^{-1}).
}
\tag{22}
\]

Equivalently, for sufficiently large `n`,

\[
\boxed{
\left|a_n\log r-b_n\log s\right|
\ll_{r,s,B}x_n^{-1}.
}
\tag{23}
\]

The fixed ladder normalization, the `1/j` correction, and the Lambert-`W` transform have all disappeared. This is stronger than what follows from a direct asymptotic comparison of the event coordinates.

## 3. Matveev turns `O(1/x)` synchronization into an event-scale power jump

Since `r` and `s` are distinct primes, they are multiplicatively independent. Thus

\[
\Lambda=a\log r-b\log s
\]

is nonzero for positive integers `a,b`.

A standard fixed-number consequence of Matveev's explicit lower bound for linear forms in logarithms of algebraic numbers gives effectively computable constants

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
\tag{24}
\]

Apply (24) to `(a_n,b_n)` and combine with (23). Then

\[
m_n^{C_0}\gg_{r,s,B}x_n,
\]

so (5) holds, for example, with

\[
\boxed{
\delta_{r,s}=C_0(r,s)^{-1}>0.
}
\tag{25}
\]

The qualitative consequence is much more important than the numerical value of this exponent. From the fixed-ladder asymptotic already derived in `RE-019`,

\[
\log x_n=j_n\log r+O_r(\log j_n),
\tag{26}
\]

and therefore a positive power of `x_n` is exponential in `j_n`, giving (6).

The logarithmic-form theorem is still used only at the **increment level between two successive collisions**. It is not a direct lower bound for a single Lambert-`W` event gap and does not solve the Alaoglu--Erdos exact simultaneous-jump problem.

## 4. Event-scale jumps make the collision set iterated-logarithmically sparse

Bounded collisions synchronize the two depths. As in `RE-019`, taking logarithms in the fixed-ladder growth law gives

\[
k_n
=
\frac{\log r}{\log s}\,j_n
+O_{r,s,B}(\log j_n),
\tag{27}
\]

so `j_n` and `k_n` are comparable.

If `m_n=a_n`, then `j_(n+1)>=m_n`. If `m_n=b_n`, then `k_(n+1)>=m_n`, and (27) at `n+1` again gives `j_(n+1)\gg_(r,s)m_n`. Thus (5) implies

\[
j_{n+1}\gg_{r,s,B}x_n^{\delta_{r,s}}.
\tag{28}
\]

Using (26) at `n+1`, after increasing the starting threshold if necessary,

\[
\log x_{n+1}
\gg_r j_{n+1}
\gg_{r,s,B}x_n^{\delta_{r,s}},
\]

which is (7).

Put `u_n=log x_n`. Then (7) reads

\[
u_{n+1}\ge c\,e^{\delta u_n}.
\tag{29}
\]

After discarding a fixed initial segment and rescaling by a constant depending only on `r,s,B`, (29) dominates

\[
v_{n+1}\ge e^{v_n}.
\tag{30}
\]

Therefore the number of terms with `u_n<=log Z` is at most an additive constant plus the number of logarithms required to descend from `log Z` to a fixed threshold. This proves (8).

For the full set of collision pairs rather than a preselected subsequence, no hidden multiplicity changes the bound. A fixed event ladder has `eta_(r,j+1)/eta_(r,j)->r>1`, so its additive spacing eventually exceeds `B`. Hence, beyond a fixed threshold, a given left-ladder event has at most one right-ladder partner within distance `B`, and ordering all such pairs by the left coordinate also orders the right coordinate. The argument above therefore applies to the entire tail of the collision set.

## 5. Transfer to bounded ordinary-prime envelopes

Fix `G>0`. `RE-018` proves that every prime factor appearing at either boundary of a sufficiently large regular self-tangent CA local peak with `g(C)<=G` lies in the finite set

\[
\mathcal P_G
=
\{r\text{ prime}:r<e^{2G+3}\},
\tag{31}
\]

and that the two adjacent transition coordinates differ by less than `G+1`.

Choose one boundary atom deterministically at each side of each peak, as in `RE-019`. This partitions all sufficiently large peaks into finitely many ordered pairs of distinct bases `(r,s)` from `mathcal P_G`. For each pair, apply (8) with `B=G+1`. A peak with `X<=Z` has right boundary below `Z+G+1`, which does not alter an iterated-logarithm count. Summing over the finite set of ordered base pairs proves (9).

Thus the fixed-envelope escape is now extremely rigid: an infinite family cannot merely hop through a sparse set of deep near-collisions. Successive synchronizations of the same two fixed prime-power ladders must be separated by a positive power of the **current event coordinate**, forcing tower-like growth of the candidate host coordinates.

## 6. Prior-art and novelty boundary

The Diophantine input is classical. Matveev's theorem gives explicit lower bounds for nonzero integer linear forms in logarithms of fixed algebraic numbers, and (24) is its standard two-logarithm specialization to the multiplicatively independent rational integers `r` and `s`. No novelty is claimed for Baker's method, irrationality measures for `log r/log s`, or sparse intersections of exponential sequences.

The closest CA-specific obstruction remains Alaoglu--Erdos's discussion of simultaneous exponent jumps. Their theorem controls the prime-exponent thresholds and records the unresolved two-prime simultaneous-rationality issue behind exact ties. That problem concerns one event parameter and is not solved here.

A targeted audit of current colossally abundant transition literature and searches combining CA transitions with linear forms in logarithms did not locate the successive-collision identity (22). The mathematical delta is narrower: the exact CA parameter `A=eta log eta=log r/lambda_(r,j)` lets two bounded event-coordinate collisions be divided **before** applying Lambert-`W` asymptotics. This cancels the fixed event normalization and leaves the homogeneous increment form with `O(1/x)` accuracy. Combined with the classical logarithmic-form lower bound, it yields

\[
\text{bounded CA event collisions}
\Longrightarrow
\text{event-scale power layer jumps}
\Longrightarrow
\text{iterated-logarithmic bounded-envelope host count}.
\]

`SOURCES.md` already records Matveev as the load-bearing external theorem, so no additional source anchor is required.

## 7. Boundaries and research consequence

Equation (9) is still a **host-set restriction**, not an exclusion theorem. `log^* log Z` is unbounded, however slowly, so an infinite Robin-counterexample subsequence is not logically excluded. The result also requires a fixed ordinary-envelope bound `G`; it gives no uniform separation when `g(C)` grows with `X` because both the allowed base set and the collision-width constant then vary.

Nothing here controls the selected mixed prime race on the finite intermediate annulus of `RE-014`--`RE-015`. In particular, sparsity of candidate event hosts does not imply that the mixed-race value at those hosts has the sign needed for Robin. The theorem also gives no lower bound showing `|eta_(r,j)-eta_(s,k)|->infinity` for every single pair `(j,k)`, and it does not remove exact/tied higher-layer transitions.

The bounded-envelope branch is nevertheless reduced to an extremely sparse Diophantine escape. A genuine closure now needs one of three additional ingredients: a single-collision separation theorem ruling out all but finitely many bounded near-collisions for fixed bases; a source-specific argument showing that the CA-selected mixed-race threshold cannot recur on this super-lacunary host set; or an independent Robin-extremal argument forcing any hypothetical counterexample sequence into a bounded envelope and then excluding the remaining ladder synchronization. Growing envelopes remain a separate chamber.