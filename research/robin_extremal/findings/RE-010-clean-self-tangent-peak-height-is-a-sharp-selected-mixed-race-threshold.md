# RE-010 — clean self-tangent peak height is a sharp selected mixed-race threshold

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + EXPONENT-TAIL-ASYMPTOTIC + TWO-SIDED-HEIGHT-DICTIONARY + SELECTED-MIXED-RACE-THRESHOLD + PRIOR-ART-ALIGNED`. `RE-008` couples the exact clean self-tangent selector to the Robin height and proves that every unbounded clean counterexample sequence forces

\[
\sqrt p\log p\,\mathcal M_*(p)\ge 2\sqrt2-o(1),
\]

but its exponent-tail analysis was deliberately one-sided: it established only

\[
\liminf \sqrt p\log p\,T(C)\ge\sqrt2.
\]

The same CA layer geometry actually fixes that tail to first order. For every unbounded sequence of sufficiently large **clean regular self-tangent CA local peaks** `C`, with `X=log C` and consecutive first-layer boundary primes `p<X<q`, one has

\[
\boxed{
\sqrt p\log p\,T(C)\longrightarrow\sqrt2.
}
\tag{1}
\]

Consequently the exact height identity of `RE-008` becomes the two-sided asymptotic

\[
\boxed{
\sqrt p\log p\,\bigl(\log G(C)-\gamma\bigr)
=
\mathscr Y(p)-2\sqrt2+o(1),
}
\tag{2}
\]

where

\[
\mathscr Y(p)
:=\sqrt p\log p\,\mathcal M_*(p)
\]

is the mixed reciprocal/standard prime-race coordinate identified in `RE-009`. Thus, inside the clean self-tangent chamber, the asymptotic Robin sign is no longer obscured by an uncontrolled CA truncation term: it is exactly the sign of one **source-selected mixed-race threshold** relative to `2sqrt(2)`.

In particular, for every fixed `delta>0`, along any such clean peak sequence,

\[
\mathscr Y(p)\le2\sqrt2-\delta
\quad\Longrightarrow\quad
G(C)<e^\gamma
\quad\text{eventually},
\tag{3}
\]

while

\[
\mathscr Y(p)\ge2\sqrt2+\delta
\quad\Longrightarrow\quad
G(C)>e^\gamma
\quad\text{eventually}.
\tag{4}
\]

This does not bound `mathscr Y` on the selected primes. By `RE-009`, even a global one-sided bound for that mixed coordinate would already be RH-equivalent. The remaining clean-chamber theorem is therefore exactly selection-specific: show that boundary primes satisfying the CA self-tangent/clean-peak selector cannot cross the threshold in (4) infinitely often, or force hypothetical counterexamples into the higher-layer/tied chamber of `RE-004`.

## 1. The exponent tail is determined by the first inactive CA layer

Retain the notation of `RE-008`. Write

\[
C=\prod_{r\le p}r^{a_r},
\qquad
T(C)
=-\sum_{r\le p}\log\!\left(1-r^{-(a_r+1)}\right).
\tag{5}
\]

For a prime `r` and integer `j>=1`, put

\[
t_{r,j}:=-\log(1-r^{-j}),
\qquad
\lambda_{r,j}
:=\log\frac{1-r^{-(j+1)}}{1-r^{-j}}
=t_{r,j}-t_{r,j+1}.
\tag{6}
\]

The CA event location `eta_(r,j)` is defined by

\[
\frac1{\eta_{r,j}\log\eta_{r,j}}
=\frac{\lambda_{r,j}}{\log r}.
\tag{7}
\]

At the regular self-tangent coordinate `X`, the exponent `a_r` is exactly the number of active layers of `r`. Hence the next layer `j=a_r+1` is inactive and

\[
\eta_{r,a_r+1}>X.
\tag{8}
\]

Because `x mapsto 1/(x log x)` is decreasing,

\[
\boxed{
\lambda_{r,a_r+1}
<\frac{\log r}{X\log X}.
}
\tag{9}
\]

This gives a useful uniform bound for primes whose second layer is already active. If `a_r>=2`, then `j=a_r+1>=3`. Put `x=r^{-j}`. Since `r>=2` and `j>=3`, `x/r<=1/16`, and the elementary logarithm bounds give

\[
t_{r,j+1}
\le\frac{x/r}{1-x/r}
\le\frac{8}{15}x
\le\frac{8}{15}t_{r,j}.
\tag{10}
\]

Therefore

\[
\lambda_{r,j}
=t_{r,j}-t_{r,j+1}
\ge\frac7{15}t_{r,j},
\]

so, using (9),

\[
\boxed{
-\log\!\left(1-r^{-(a_r+1)}\right)
\le3\frac{\log r}{X\log X}
\qquad(a_r\ge2).
}
\tag{11}
\]

We will combine this source-sensitive bound with the trivial cubic decay coming from `a_r+1>=3`.

## 2. Primes with exponent at least two contribute below square-root scale

Let

\[
T_{\ge2}(C)
:=\sum_{\substack{r\le p\\a_r\ge2}}
-\log\!\left(1-r^{-(a_r+1)}\right).
\tag{12}
\]

For `a_r>=2`, besides (11),

\[
-\log\!\left(1-r^{-(a_r+1)}\right)
\ll r^{-3}.
\tag{13}
\]

Split the prime sum at `z=X^(1/3)`. Chebyshev's elementary bound `vartheta(z)=O(z)` and (11) give

\[
\sum_{\substack{r\le z\\a_r\ge2}}
-\log\!\left(1-r^{-(a_r+1)}\right)
\ll
\frac{\vartheta(z)}{X\log X}
\ll\frac{X^{-2/3}}{\log X}.
\tag{14}
\]

For the complementary range, (13) and comparison with the integer tail give

\[
\sum_{\substack{z<r\le p\\a_r\ge2}}
-\log\!\left(1-r^{-(a_r+1)}\right)
\ll\sum_{n>z}n^{-3}
\ll X^{-2/3}.
\tag{15}
\]

Thus

\[
\boxed{
T_{\ge2}(C)=O(X^{-2/3}),
}
\tag{16}
\]

and, since `p/X->1` along clean peaks,

\[
\boxed{
\sqrt p\log p\,T_{\ge2}(C)\longrightarrow0.
}
\tag{17}
\]

This estimate is where the exact CA threshold condition matters. Bounding every small-prime truncation term merely by `r^-3` would leave a fixed positive contribution and lose the Robin scale. The first-inactive-layer inequality (9) supplies the missing uniform decay.

## 3. Exponent-one primes give exactly the `sqrt(2)` truncation tax

Let

\[
T_1(C)
:=\sum_{\substack{r\le p\\a_r=1}}
-\log(1-r^{-2}).
\tag{18}
\]

`RE-007` proves the second-layer asymptotic

\[
\eta_{r,2}=\frac{r^2}{2}(1+o(1))
\tag{19}
\]

and uses it in a uniform threshold sandwich. For every fixed `epsilon in (0,1)`, define

\[
y_-(X):=\sqrt{\frac{2X}{1+\varepsilon}},
\qquad
y_+(X):=\sqrt{\frac{2X}{1-\varepsilon}}.
\tag{20}
\]

For all sufficiently large `X`, every prime `r<=y_-(X)` has its second layer active and hence `a_r>=2`; every prime `y_+(X)<r<=p` has its second layer inactive and hence `a_r=1`. Therefore

\[
\sum_{y_+(X)<r\le p}-\log(1-r^{-2})
\le T_1(C)
\le
\sum_{y_-(X)<r\le p}-\log(1-r^{-2}).
\tag{21}
\]

Uniformly in these tails,

\[
-\log(1-r^{-2})=r^{-2}+O(r^{-4}).
\tag{22}
\]

The prime number theorem and partial summation give

\[
\sum_{r>y}\frac1{r^2}
\sim\frac1{y\log y}.
\tag{23}
\]

The omitted tail above `p` is asymptotic to `1/(p log p)` and therefore vanishes after multiplication by `sqrt(p) log p`; the error term in (22) is smaller still. Since `p/X->1`, equations (20)--(23) yield

\[
\sqrt{2(1-\varepsilon)}
\le
\liminf\sqrt p\log p\,T_1(C)
\]

and

\[
\limsup\sqrt p\log p\,T_1(C)
\le
\sqrt{2(1+\varepsilon)}.
\tag{24}
\]

Letting `epsilon downarrow0` gives

\[
\boxed{
\sqrt p\log p\,T_1(C)\longrightarrow\sqrt2.
}
\tag{25}
\]

Together with (17), this proves (1).

The source of the constant is now exact. The first inactive exponent correction is dominated by primes just beyond the second-layer CA frontier `r~sqrt(2X)`, and the reciprocal-square prime tail contributes `1/(sqrt(2X) log sqrt(2X))`, which becomes `sqrt2` after the natural Robin normalization.

## 4. The clean Robin height has a two-sided selected-race asymptotic

`RE-008` proves the exact identity

\[
\log G(C)-\gamma
=
\mathcal M_*(p)
-T(C)
-\Phi_{\ge2}(X)h(p)
+Q(p,X),
\tag{26}
\]

with

\[
\sqrt p\log p\,Q(p,X)\to0
\tag{27}
\]

and

\[
\sqrt p\log p\,\Phi_{\ge2}(X)h(p)
\to\sqrt2.
\tag{28}
\]

Multiplying (26) by `sqrt(p) log p`, then inserting (1), (27), and (28), proves (2).

By `RE-009`, the remaining source coordinate has the exact normalization dictionary

\[
\mathscr Y(p)
=\mathcal E_{\pi_\ell}(p)
-\lambda(p)\mathcal E_\vartheta(p),
\qquad
\lambda(p)=-p\log(1-p^{-1})=1+o(1),
\tag{29}
\]

and hence

\[
\mathscr Y(p)
=\mathcal E_{\pi_\ell}(p)-\mathcal E_\vartheta(p)+o(1).
\tag{30}
\]

Thus the clean self-tangent CA selector determines **where** the classical mixed prime race is sampled, while (2) determines **exactly what threshold** its selected value must cross to change the Robin sign.

Equation (2) is stronger than the one-sided counterexample implication of `RE-008`. It applies to every unbounded clean regular self-tangent CA local-peak sequence, safe or violating. The only unresolved first-order quantity is `mathscr Y(p)` itself at the selected boundary primes.

## 5. Prior art and calibration

The square-root correction in divisor-sum extremality is classical. Ramanujan's expansion, as treated by Jean-Louis Nicolas and already anchored in `SOURCES.md`, contains the coefficient `2(sqrt(2)-1)` at the corresponding scale. Robin's RH analysis of colossally abundant values likewise produces the familiar combination `2(1-sqrt(2))` plus the zero-term/bias contribution. No novelty is claimed for those constants or for the reciprocal-square prime-tail asymptotic.

The present formula is consistent with that classical boundary in a precise way. `RE-009` records from Bhattacharya--Martin--Simpson that under RH

\[
2-w
\le\liminf\mathscr Y(x)
\le\limsup\mathscr Y(x)
\le2+w,
\qquad
w=2+\gamma-\log(4\pi).
\tag{31}
\]

Combining the upper edge of (31) with (2) gives the clean-peak coefficient

\[
2+w-2\sqrt2
=2(1-\sqrt2)+w,
\tag{32}
\]

which is exactly the classical Robin/Ramanujan combination. This is a **consistency calibration only**: RH already excludes Robin counterexamples and is not used in the unconditional derivation (1)--(2).

Marco Mantovanelli's August 2026 preprint is the closest representation-level prior art for the self-tangent event measure and a square-root prime-frontier decomposition. The public companion explicitly certifies finite prime-frontier identities but is not used as a premise here. A targeted audit did not identify in the available source record an unconditional two-sided formula in the exact selected mixed-race form (2); the finding should therefore be read as a Mathia-specific recombination of classical/event-layer ingredients, not as a claim that the square-root CA asymptotics themselves are new.

No new source anchor is required: the non-elementary ingredients are already represented in `SOURCES.md` by Alaoglu--Erdos/Robin, Nicolas, Mantovanelli, and Bhattacharya--Martin--Simpson.

## 6. Boundaries and research consequence

The **clean first-layer boundary** hypothesis is load-bearing. If either adjacent CA transition contains a higher layer or a tie, `RE-006`'s consecutive-prime selector and the clean height splice do not apply. Those peaks remain in the exceptional chamber isolated by `RE-004`.

Regular self-tangency is also load-bearing in (8)--(11): the exponent of each prime is exactly the count of active CA layers at the same intrinsic coordinate `X`. An arbitrary integer with the same largest prime need not satisfy the first-inactive-layer estimate and need not have the truncation asymptotic (1).

Equation (2) does **not** supply an unconditional bound on the mixed prime race. `RE-009` proves that a global one-sided bound for that coordinate is already RH-equivalent, so the route cannot be closed by forgetting the selector. Nor does transition-count zero density in `RE-004` prevent all hypothetical counterexample peaks from concentrating on the exceptional chamber.

What (2) does close is the remaining first-order bookkeeping ambiguity in the clean chamber. A complete continuation no longer needs to estimate an unknown exponent-tail coefficient. It must attack one of two genuinely source-specific statements: prove that CA-selected clean boundary primes cannot realize `mathscr Y(p)>=2sqrt(2)+o(1)` infinitely often, or prove that hypothetical counterexample peaks cannot concentrate on higher-layer/tied transition boundaries. The first is a selected mixed-prime-race correlation problem; the second is an exceptional-event concentration problem. Neither is replaced by a global prime-race or global workload bound.