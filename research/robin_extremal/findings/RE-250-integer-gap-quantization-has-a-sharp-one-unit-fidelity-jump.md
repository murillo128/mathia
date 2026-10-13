# RE-250 — Integer gap quantization has a sharp one-unit source-fidelity jump

**Status:** EXACT-DERIVED + INTEGER-LABEL-QUANTIZATION + SHARP-MATCHED-SOURCE-OBSTRUCTION + PRIOR-ART-BOUNDED; independent adversarial audit pending.

**Parent findings:** RE-247, RE-248, RE-249; integer-label and divisor-sum realization boundaries RE-056, RE-057.

RE-249 gives a continuous sharp modulus for terminal Robin-source ambiguity when generalized-prime labels are real and the absolute change in *every consecutive gap* is at most a vanishing tolerance. Requiring the labels to be integers changes that fidelity metric discontinuously. Below one unit, there is no nontrivial rank-preserving transport at all; already at one unit, however, integer-rounded transports attain the entire PNT-envelope ambiguity of RE-247. This is a quantization theorem for integer-valued **generalized-prime labels**, not for genuine prime numbers or ordinary divisor sums.

## 1. Exact integer-gap threshold and sharp ambiguity

Fix \(b>0\), \(0<\alpha<3/4\), and \(p\to\infty\), with \(U=U(p)\) satisfying \(U/p\to\infty\). Put
\[
 a=e^{-2},\quad T=aU,\quad
 V(t)=\frac{(\log t)^{3/5}}{(\log\log t)^{1/5}},\quad
 E(t)=t\,e^{-bV(t)},\quad E_U=E(U),
 \tag{1}
\]
\[
 B_{p,b,U}
 =\frac{\sqrt p\log p}{\log U}e^{-bV(U)},
 \qquad
 \eta_{\rm crit}=(\log U)e^{-bV(U)}.
 \tag{2}
\]
Here \(E_U\to\infty\), \(E_U/U\to0\), and \(\eta_{\rm crit}\to0\).

There exists a **single fixed** strictly increasing sequence of positive integers
\(Q_{\mathbb Z}=(q_j)_{j\ge1}\), and a fixed \(t_0=t_0(b)\), such that
\[
q_{j+1}-q_j=\log q_{j+1}+O(1),\qquad
\vartheta_{Q_{\mathbb Z}}(t)=t+O(\log t),\quad
\vartheta_Q(t):=\sum_{r\in Q,\ r\le t}\log r,
\tag{3}
\]
and the baseline obeys the unit all-height envelope
\[
|\vartheta_{Q_{\mathbb Z}}(t)-t|\le E(t)
\qquad(t\ge t_0).
\tag{4}
\]

For each \(\eta=\eta_U\ge0\), call an indexed sequence
\(R=(r_j)\) an **integer admissible transport** when

1. the \(r_j\) are strictly increasing integers \(>1\), with \(r_j=q_j\) for \(q_j\notin(T,U)\), while every remaining \(r_j\) stays in \((T,U)\);
2. the *same* \(t_0\) and *unit* bound (4) hold for \(R\) at every \(t\ge t_0\);
3. for every consecutive pair, including shell-straddling pairs,
   \[
   |(r_{j+1}-r_j)-(q_{j+1}-q_j)|\le\eta.
   \tag{5}
   \]

Use exactly the RE-247--RE-249 normalized truncated source observable:
\[
h(t)=\frac{-\log(1-t^{-1})}{\log t},\qquad
Z_{p,U}=\sqrt p\log p\int_{p+p^\alpha}^{U}
\sqrt t\,(-h'(t))\,dt=2+o(1),
\tag{6}
\]
\[
\mathcal A_{p,U}(R)=\frac{\sqrt p\log p}{Z_{p,U}}
\int_{p+p^\alpha}^{U}
(t-\vartheta_R(t))(-h'(t))\,dt.
\tag{7}
\]
Let \(\Delta^{\mathbb Z}_{p,b,U}(\eta)\) be the supremum of
\(|\mathcal A(R^1)-\mathcal A(R^2)|\) over pairs of integer admissible
transports of this same fixed baseline.

**Theorem (one-unit integer-fidelity transition).**
For every sufficiently large \(p\) and every \(0\le\eta<1\),
\[
\boxed{\Delta^{\mathbb Z}_{p,b,U}(\eta)=0.}
\tag{8}
\]
For any choice of \(\eta=\eta_U\ge1\), allowing \(\eta_U\) to depend arbitrarily on \(p\),
\[
\boxed{\Delta^{\mathbb Z}_{p,b,U}(\eta)
       =(2+o(1))B_{p,b,U}.}
\tag{9}
\]
The error in (9) is uniform in \(\eta\ge1\), since the same pair of
transports with gap changes at most **one integer unit** attains its lower
bound; RE-247 supplies the uniform upper bound.

Thus the continuous RE-249 scale
\(\eta_{\rm crit}=(\log U)e^{-bV(U)}=o(1)\) has **no analogous gradual
transition under absolute integer-gap fidelity**: the allowable family
collapses identically for \(\eta<1\), but at \(\eta=1\) already retains the
full \((2+o(1))B_{p,b,U}\) ambiguity. The comparison is within a matched
integer-valued generalized-prime class, not within the ordinary primes.

## 2. A fixed integer source with an all-height PNT envelope

Start with RE-247's fixed real source \((x_j)\), defined by
\[
x_1=2,\qquad x_{j+1}-\log x_{j+1}=x_j.
\tag{10}
\]
The strictly increasing inverse of \(x\mapsto x-\log x\) on \(x>1\)
defines all \(x_j\), with gaps \(x_{j+1}-x_j=\log x_{j+1}>1\).
Summing these gaps yields
\[
\vartheta_X(x_j)=x_j-(2-\log2),\qquad
\vartheta_X(t)=t+O(\log t).
\tag{11}
\]

Set \(q_j=\lfloor x_j\rfloor\). Since every real gap is \(>1\),
these are distinct, strictly increasing integers; rounding each endpoint
changes a consecutive gap by at most one in absolute value. It follows that
\[
q_{j+1}-q_j=\log q_{j+1}+O(1).
\tag{12}
\]
The change in the logarithmic weight of a label is
\[
|\log q_j-\log x_j|\ll x_j^{-1}.
\tag{13}
\]
From the baseline gaps, the number of points in a dyadic interval at
scale \(y\) is \(O(y/\log y)\). Summation over dyadic scales gives
\[
\sum_{x_j\le t+1}\frac1{x_j}=O(\log\log t).
\tag{14}
\]
At any threshold \(t\), at most one rounded label may have crossed the
threshold from the interval \((t,t+1]\); its weight is \(O(\log t)\).
Thus (11)--(14) prove
\[
\vartheta_{Q_{\mathbb Z}}(t)
=\vartheta_X(t)+O(\log t)=t+O(\log t).
\tag{15}
\]
Because \(E(t)/\log t\to\infty\), select a fixed \(t_0(b)\) such that
\[
|\vartheta_{Q_{\mathbb Z}}(t)-t|\le E(t)/4
\qquad(t\ge t_0).
\tag{16}
\]
The shell \((T,U)\) has \(O(U/\log U)\) labels; every baseline gap on
this fixed multiplicative shell, including the two straddling gaps, is
\(\log U+O(1)\). These facts do not depend on \(p\).

## 3. Quantized gaps below one unit freeze every label

For an integer transport write \(d_j=r_j-q_j\in\mathbb Z\).
The difference of consecutive gaps in (5) is exactly
\[
(r_{j+1}-r_j)-(q_{j+1}-q_j)=d_{j+1}-d_j\in\mathbb Z.
\tag{17}
\]
If \(\eta<1\), this integer must vanish at every index. All \(d_j\)
are therefore equal, and the exact exterior matching makes their common
value zero. The only admissible source is \(Q_{\mathbb Z}\) itself,
proving (8). This argument needs no PNT assumption; the
all-height quantitative PNT constraint becomes relevant only to
the sharpness construction above the one-unit threshold.

## 4. Round a maximally separated real transport without exceeding one gap unit

Write, as in RE-249,
\[
f_M(u)=\min\{u,M(u-a),M(1-u)\}\quad(a\le u\le1),
\tag{18}
\]
extended by zero outside \([a,1]\), and
\[
C(M)=\int_a^1\frac{f_M(u)}{u^2}\,du,\quad
0\le C(M)<2,\quad C(M)\longrightarrow2\ (M\to\infty).
\tag{19}
\]
The extension is globally \(M\)-Lipschitz, is nonnegative, vanishes at
both endpoints, and is bounded above by \(u\).

Choose, independently of the allowed tolerance \(\eta\ge1\),
\[
\delta=(\log U)^{-1/2},\quad
\lambda=1-\delta,\quad
M=\frac1{4\eta_{\rm crit}}
=\frac{U}{4E_U\log U}\longrightarrow\infty.
\tag{20}
\]
Define *integer* displacements and two transports by
\[
s_j=\lambda E_U f_M(q_j/U),\qquad
k_j=\left\lfloor s_j+\frac12\right\rfloor,\qquad
r_j^\pm=q_j\pm k_j.
\tag{21}
\]
Outside the shell \(s_j=k_j=0\).

By the Lipschitz bound and (20), for consecutive labels at the shell
or its boundaries,
\[
|s_{j+1}-s_j|
\le\lambda \frac{E_U M}{U}(q_{j+1}-q_j)
=\lambda\frac{q_{j+1}-q_j}{4\log U}
=\frac14+o(1)<\frac13.
\tag{22}
\]
Two numbers less than one apart cannot have nearest-integer roundings
differing by more than one. Hence
\[
|k_{j+1}-k_j|\le1,\qquad
|(r_{j+1}^\pm-r_j^\pm)-(q_{j+1}-q_j)|\le1.
\tag{23}
\]
All transported gaps remain strictly positive because the baseline
gaps in the shell tend to infinity, and outside the shell they are
unchanged. Near the endpoints,
\[
s_j\le\frac{\lambda}{4\log U}
\min\{q_j-T,U-q_j\}\quad(T<q_j<U).
\tag{24}
\]
If \(k_j\ge1\), then \(s_j\ge1/2\), so (24) implies that both boundary
distances greatly exceed \(k_j\) for sufficiently large \(U\);
otherwise \(k_j=0\). Thus no label crosses \(T\) or \(U\).
The transports preserve exact exterior labels, rank, shell
cardinality, distinctness, and (23), including all straddling gaps.

Moreover
\[
k_j=\lambda E_U f_M(q_j/U)+O(1),\qquad
D:=\max_j k_j\le E_U+O(1)=o(U).
\tag{25}
\]
This last rounding error is essential: it is much smaller than the
PNT margin and negligible in the terminal kernel, although the *gap*
distortion has been quantized to an integer.

## 5. The same unit PNT envelope survives the integer rounding

For every \(q_j\) in the shell, let
\[
W_j^\pm=
\sum_{\substack{k:\ q_k\le q_j\\q_k\in(T,U)}}
\log\frac{r_k^\pm}{q_k}.
\tag{26}
\]
All old and new shell labels lie in \((T,U)\). Equations (12),
(15), and (25) imply
\[
|W_j^\pm|
\ll \frac{U}{\log U}\frac{D}{T}
=O(E_U/\log U).
\tag{27}
\]
At a transported jump the exact weighted-step identity is
\[
\vartheta_{R^\pm}(r_j^\pm)-r_j^\pm
=\bigl(\vartheta_{Q_{\mathbb Z}}(q_j)-q_j\bigr)
 +W_j^\pm\mp k_j.
\tag{28}
\]
Between jumps the last linear staircase contribution is at most
\(O(\log U)\), since changed consecutive gaps differ from baseline
gaps by at most one. The function \(E\) obeys
\[
E'(t)=e^{-bV(t)}(1-btV'(t))=o(1)
\tag{29}
\]
uniformly on the fixed multiplicative shell. For all shell indices,
\[
k_j\le(1-\delta)E_U(q_j/U)+O(1)
       \le(1-\delta)E(q_j)+O(1),
\tag{30}
\]
since \(V(q_j)\le V(U)\). Evaluating \(E\) at \(t\) instead of \(q_j\)
in the same transported gap changes the bound by
\(O(E_U e^{-bV(U)}+\log U)\), which is \(o(\delta E_U)\).
Combining (16), (27)--(30), uniformly for \(T\le t\le U\),
\[
|\vartheta_{R^\pm}(t)-t|
\le(1-\delta)E(t)
 +O\!\left(\log U+\frac{E_U}{\log U}
                   + E_U e^{-bV(U)}\right)
\le E(t)
\tag{31}
\]
for sufficiently large \(U\). Here \(E(t)\asymp E_U\) on the shell,
\(\delta\gg1/\log U\) and
\(E_Ue^{-bV(U)}=o(\delta E_U)\); the strict margin is uniform.

For \(t<T\) the labels equal the fixed baseline, already covered by
(16). For \(t\ge U\) all labels again coincide with the baseline, and
the *only* residual discrepancy in their accumulated logarithmic
weights is \(W_\infty^\pm=O(E_U/\log U)\). Since \(E(t)\) is eventually
increasing and the baseline uses only a quarter of the envelope,
\[
|\vartheta_{R^\pm}(t)-t|
\le E(t)/4+O(E_U/\log U)\le E(t)
\qquad(t\ge U).
\tag{32}
\]
Both transports therefore satisfy the same unit quantitative-PNT
bound at every \(t\ge t_0\), with no dependence of \(t_0\) on \(U\)
or the choice of sign.

## 6. Exact positive source subtraction attains the full constant

As RE-249 derives without replacing transported logarithmic weights,
for shell-supported indexed transports the source-difference identity is
\[
\mathcal A(R^+)-\mathcal A(R^-)
=\frac{\sqrt p\log p}{Z_{p,U}}
\sum_{q_j\in(T,U)}
\int_{q_j-k_j}^{q_j+k_j}
\left(\frac1{r(r-1)}+\frac{h(U)}r\right)dr.
\tag{33}
\]
Every summand is nonnegative. Uniformly across the shell, because
\(k_j=O(E_U)=o(U)\),
\[
\frac1{r(r-1)}+\frac{h(U)}r
=\frac{1+O(E_U/U+1/\log U)}{q_j^2}.
\tag{34}
\]
The rounding errors in (25) contribute
\[
\sum_{q_j\in(T,U)}
\frac{O(1)}{q_j^2}
=O\!\left(\frac1{U\log U}\right)
=o\!\left(\frac{e^{-bV(U)}}{\log U}\right).
\tag{35}
\]

The fixed *integer* baseline still has mesh
\(q_{j+1}-q_j=\log U+O(1)\) on the shell. Positive quadrature,
including the narrow obstacle ramps, yields
\[
\sum_{q_j\in(T,U)}
\frac{E_U f_M(q_j/U)}{q_j^2}
=
\frac{e^{-bV(U)}}{\log U}\bigl(C(M)+o(1)\bigr).
\tag{36}
\]
Indeed \(f_M(u)/u^2\) has uniformly bounded total variation
for all \(M\ge1\), the scaled mesh is \(O(\log U/U)\), and relative
gap-to-\(\log U\) errors are \(O(1/\log U)\).
Even as \(M\to\infty\), the ramps remain resolved, and
\(C(M)\to2\) by dominated convergence.

Use (25), (33)--(36), \(\lambda\to1\), and \(Z_{p,U}\to2\) to obtain
\[
\mathcal A(R^+)-\mathcal A(R^-)
=\frac{\sqrt p\log p}{Z_{p,U}}\,
2\lambda\frac{e^{-bV(U)}}{\log U}
\bigl(C(M)+o(1)\bigr)
=(2+o(1))B_{p,b,U}.
\tag{37}
\]
The common unit PNT envelope and exact common prefix place this pair
inside RE-247's unrestricted comparison class; its upper bound gives
\(\Delta^{\mathbb Z}\le(2+o(1))B_{p,b,U}\). Equation (37) gives the
matching lower bound, establishing (9).

## 7. Prior-art boundary and falsification controls

The implication \(|d_{j+1}-d_j|<1\Rightarrow d_{j+1}=d_j\)
for integer displacements is elementary arithmetic, not a new
number-theoretic lemma. Monotone quantile transport, nearest-integer
rounding, and generalized-prime source flexibility are classical
backgrounds. The specific new *line-local synthesis* is the sharp
discontinuity for RE-247's **fully normalized terminal Robin kernel**
under exact exterior matching, all-height unit PNT fidelity, fixed
integer rank, and an absolute bound on each neighboring gap.
In particular, it takes the continuous RE-249 obstacle extremizer,
rounds its *individual positions* while rigorously preserving both
the all-height logarithmic-weight envelope and a one-unit gap budget,
and matches RE-247's constant 2.

RE-056 already established that integer-label generalized-prime
controls can reproduce certain all-layer CA support chambers; it did
not impose this terminal-kernel observable or absolute gap-fidelity
metric. RE-057 shows the decisive independent limitation: composite
integer labels cannot act as ordinary prime atoms for the actual
\(\sigma(n)\) gain; the error is at least square-root scale. The
Diamond--Zhang general Beurling source literature
(*Optimality of Chebyshev bounds for Beurling generalized numbers*,
Acta Arith. 160 (2013), 259--275, DOI 10.4064/aa160-3-3)
concerns counting bounds, not this quantized terminal comparison.
No novelty is claimed for the elementary rounding principle or
for generalized-prime perturbations alone, and an independent
novelty/proof audit is still warranted. No new load-bearing
external theorem or SOURCES.md edit is needed.

Essential failure checks are: retain the **identical** indexed exterior
source when proving the \(\eta<1\) freeze; verify rounded labels remain
strictly increasing and inside both endpoints; include gap pairs
straddling the shell; retain changed logarithmic weights (27)--(28)
rather than transporting only jump positions; verify the unit PNT
envelope for **every** \(t\ge t_0\), including \(t>U\); bound the
accumulated rounding error by (35), not by an uncontrolled difference
of separate staircases; preserve the upper-endpoint correction
\(h(U)\) and \(Z_{p,U}\to2\); and never identify the integer
generalized labels with genuinely prime integers.

The implication for the Robin program is a boundary on the
information supplied by source-fidelity metrics. Integer
quantization makes a subunit absolute gap-error bound vacuously
rigid, whereas a one-unit bound is still compatible with maximum
terminal ambiguity. This does not restrict the actual CA
counterexample selector, supply an ordinary-prime-only estimate,
prove any new inequality for \(\sigma(n)\), or establish RH.
