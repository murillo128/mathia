# FD-042 — critical Mellin packets have universal nonsquarefree Jordan occupation

**Status:** `EXACT-DERIVED + CRITICAL-MELLIN-PACKET + NONSQUAREFREE-JORDAN-FRAME + UNIVERSAL-OCCUPATION + HYPERBOLA-SAMPLING-BOUNDARY + PHYSICAL-SOURCE-CONDITIONAL`.

`FD-040` proves that every fixed finite Mellin-frequency packet with real exponent `beta>1/2` has a positive nonsquarefree Jordan-frame constant, but leaves the critical exponent `beta=1/2` outside the argument because the row norm is then logarithmically divergent. `FD-038` independently proves the universal weighted nonsquarefree density

\[
\delta_{\mathrm{ns}}
=1-\zeta(3)
\prod_p(1-p^{-2}-p^{-3}+p^{-4})
=0.3558\ldots
\]

on sufficiently long terminal quotient blocks.

At the critical Mellin exponent these two mechanisms meet exactly. For every fixed finite set of distinct logarithmic frequencies, the full and nonsquarefree critical row Gram matrices become asymptotically scalar, and their scalar ratio is precisely `delta_ns`. Consequently every shell source with a finite critical asymptotic packet

\[
F(n)=n^{1/2}(\log(en))^q\bigl(P(\log n)+o(1)\bigr),
\qquad q\ge0,
\]

where `P` is a nonzero finite real exponential sum, satisfies

\[
\boxed{
\frac{U^F_{H,D}}{E^F_{H,D}}
\longrightarrow \delta_{\mathrm{ns}}
}
\]

for every fixed Schur-head dimension `D`.

Thus the critical line is not a weak point of finite-packet coercivity. It is more rigid than the supercritical finite-packet regime: the logarithmic divergence washes out every fixed finite set of cross-frequency phases and forces the same universal occupation constant already seen in `FD-038` and `FD-041`. A physical vanishing-occupation mechanism therefore cannot come from a fixed finite critical Mellin packet either. It must use genuinely growing/infinite effective spectral complexity, collapsing frequency separation/coherence, or a different source-specific mechanism.

## 1. Critical row Gram matrices scalarize

Retain the Jordan weight

\[
w(r):=\frac{J_2(r)}{r^2}.
\tag{1}
\]

`FD-038` proves the two summatory laws

\[
W(x):=\sum_{r\le x}w(r)
=ax+O(1),
\qquad
 a:=\frac1{\zeta(3)},
\tag{2}
\]

and, for every fixed `sigma>1/2`,

\[
W_{\mathrm{ns}}(x)
:=\sum_{\substack{r\le x\\\mu(r)=0}}w(r)
=bx+O_\sigma(x^\sigma),
\tag{3}
\]

where

\[
b:=a-c_{\mathrm{sf}}>0,
\qquad
c_{\mathrm{sf}}
:=\prod_p(1-p^{-2}-p^{-3}+p^{-4}),
\tag{4}
\]

so that

\[
\frac ba=\delta_{\mathrm{ns}}.
\tag{5}
\]

Fix `D>=1` and distinct real frequencies

\[
\Gamma=\{\gamma_1,\ldots,\gamma_m\}.
\tag{6}
\]

For `R>D`, define the critical full and nonsquarefree Gram matrices

\[
G_{\mathrm{all}}^{(R)}(j,k)
:=
\sum_{D<r\le R}
\frac{w(r)}r\,
 r^{i(\gamma_j-\gamma_k)},
\tag{7}
\]

\[
G_{\mathrm{ns}}^{(R)}(j,k)
:=
\sum_{\substack{D<r\le R\\\mu(r)=0}}
\frac{w(r)}r\,
 r^{i(\gamma_j-\gamma_k)}.
\tag{8}
\]

Then

\[
\boxed{
G_{\mathrm{all}}^{(R)}
=a(\log R)I_m+O_{D,\Gamma}(1),
}
\tag{9}
\]

\[
\boxed{
G_{\mathrm{ns}}^{(R)}
=b(\log R)I_m+O_{D,\Gamma}(1),
}
\tag{10}
\]

where the errors are in operator norm.

In particular, if

\[
A_z(r):=\sum_{j=1}^m z_jr^{-i\gamma_j},
\tag{11}
\]

then uniformly over nonzero `z in C^m`,

\[
\boxed{
\frac{
\sum_{\substack{D<r\le R\\\mu(r)=0}}
 w(r)r^{-1}|A_z(r)|^2
}{
\sum_{D<r\le R}
 w(r)r^{-1}|A_z(r)|^2
}
=
\delta_{\mathrm{ns}}+O_{D,\Gamma}\!\left(\frac1{\log R}\right).
}
\tag{12}
\]

This is the critical analogue of `FD-040`, but its limiting frame constant is no longer packet-dependent.

## 2. The logarithmic diagonal beats every fixed cross-frequency term

The proof of (9)--(10) uses only the summatory laws (2)--(3). For the diagonal entries, partial summation gives

\[
\sum_{D<r\le R}\frac{w(r)}r
=a\log R+O_D(1),
\tag{13}
\]

and

\[
\sum_{\substack{D<r\le R\\\mu(r)=0}}
\frac{w(r)}r
=b\log R+O_D(1).
\tag{14}
\]

Now fix a nonzero real `t`. If an arithmetic weight has summatory function

\[
A(x)=cx+O(x^\sigma)
\qquad(\sigma<1),
\tag{15}
\]

Abel summation applied to `x^{-1+it}` gives

\[
\sum_{D<n\le R}a(n)n^{-1+it}=O_{D,t}(1).
\tag{16}
\]

Indeed the contribution of `cx` is a bounded oscillatory integral proportional to

\[
\int_D^R x^{-1+it}\,dx,
\tag{17}
\]

while the remainder contributes an absolutely convergent integral because `sigma<1`. Applying this once with (2) and once with (3) proves that every off-diagonal entry in (7)--(8) is bounded uniformly in `R`. Since `Gamma` is fixed and finite, (9)--(10) follow.

Equation (12) is then a finite-dimensional Rayleigh-quotient consequence. The smallest eigenvalue of `G_all^(R)` is `a log R+O(1)`, while

\[
G_{\mathrm{ns}}^{(R)}
-\frac ba G_{\mathrm{all}}^{(R)}
=O_{D,\Gamma}(1).
\tag{18}
\]

Dividing by the full critical norm gives the stated uniform `O(1/log R)` error.

The mechanism is worth separating from `FD-040`. For `beta>1/2`, the row sums converge and the exact phase geometry of the finite packet survives in a packet-dependent positive generalized eigenvalue. At `beta=1/2`, the diagonal terms grow like `log R` while every fixed nonzero frequency difference remains bounded. The finite packet therefore loses its phase freedom in the leading term, and only the ambient weighted row densities `a` and `b` remain.

## 3. Critical finite shell packets have an exact leading energy law

Let

\[
P(t)=\sum_{j=1}^m a_je^{i\gamma_jt}
\tag{19}
\]

be a nonzero real-valued finite exponential sum with distinct real frequencies, and fix `q>=0`. Suppose a real shell profile satisfies

\[
F(n)
=n^{1/2}(\log(en))^q
\bigl(P(\log n)+o(1)\bigr).
\tag{20}
\]

Define its exact Jordan-shell energies

\[
E^F_{H,D}
:=\sum_{D<r\le H}w(r)
F(\lfloor H/r\rfloor)^2,
\tag{21}
\]

\[
U^F_{H,D}
:=\sum_{\substack{D<r\le H\\\mu(r)=0}}w(r)
F(\lfloor H/r\rfloor)^2.
\tag{22}
\]

Then

\[
\boxed{
E^F_{H,D}
=
\left(
\frac{a}{2q+1}
\sum_{j=1}^m|a_j|^2
+o(1)
\right)
H(\log H)^{2q+1},
}
\tag{23}
\]

and

\[
\boxed{
U^F_{H,D}
=
\left(
\frac{b}{2q+1}
\sum_{j=1}^m|a_j|^2
+o(1)
\right)
H(\log H)^{2q+1}.
}
\tag{24}
\]

Their quotient is therefore (5), proving the headline occupation law.

The factor `1/(2q+1)` is the critical logarithmic volume. The finite packet contributes only its mean-square coefficient

\[
\sum_j|a_j|^2,
\tag{25}
\]

because all distinct frequency differences are lower by one logarithmic power.

## 4. Floors and the terminal rows do not change the leading term

Here is the reduction from the row Gram law to (23)--(24). Fix a large integer `K`. Split the exact energy at

\[
r\le H/K
\qquad\text{and}\qquad
r>H/K.
\tag{26}
\]

On the terminal part `r>H/K`, the quotient `floor(H/r)` is one of the finitely many integers `<K`. Hence, for fixed `K`, both total and nonsquarefree terminal contributions are

\[
O_{F,K}(H),
\tag{27}
\]

which is negligible compared with `H(log H)^(2q+1)`.

On `r<=H/K`, put `k=floor(H/r)`. Then `k>=K` and

\[
\frac{k}{H/r}=1+O(K^{-1}),
\qquad
\log k=\log(H/r)+O(K^{-1})
\tag{28}
\]

uniformly. Because `P` is a fixed finite exponential sum, it is bounded and Lipschitz. The asymptotic (20) is uniform once `k>=K` and `K` is chosen beyond its error threshold. Thus, after dividing by `H`, the bulk energy differs by an arbitrarily small relative amount from

\[
\sum_{D<r\le H/K}
\frac{w(r)}r
\bigl(1+\log(H/r)\bigr)^{2q}
\left|
P\bigl(\log H-\log r\bigr)
\right|^2.
\tag{29}
\]

For the nonsquarefree energy one restricts the same sum to `mu(r)=0`.

Set

\[
z_j(H):=a_je^{i\gamma_j\log H}.
\tag{30}
\]

Then the final factor in (29) is exactly `|A_(z(H))(r)|^2`, and

\[
\|z(H)\|_2^2=\sum_j|a_j|^2.
\tag{31}
\]

The matrix estimates (9)--(10), followed by Abel summation in the logarithmic weight `(1+log(H/r))^(2q)`, give uniformly in this phase vector

\[
\sum_{D<r\le H/K}
\frac{w(r)}r
(1+\log(H/r))^{2q}|A_{z(H)}(r)|^2
=
\left(
\frac{a}{2q+1}\|a\|_2^2+o(1)
\right)(\log H)^{2q+1},
\tag{32}
\]

and the same formula with `a` replaced by `b` on the nonsquarefree rows. Concretely, the diagonal term integrates to

\[
\int (1+\log(H/x))^{2q}\frac{dx}{x}
=
\frac{(\log H)^{2q+1}}{2q+1}
+O_{D,K,q}((\log H)^{2q}),
\tag{33}
\]

while every fixed off-diagonal frequency contributes only `O_(D,K,q,Gamma)((log H)^(2q))`. First let `H` tend to infinity and then let the fixed threshold `K` absorb the uniform `o(1)` and floor errors. This proves (23)--(24).

No zero-density estimate, RH assumption, prime-number theorem, or cancellation estimate for the shell source is used in this critical-packet theorem.

## 5. Relation to `FD-038`, `FD-040`, and `FD-041`

The constant agreement is structural. `FD-038` obtains `delta_ns=b/a` from long quotient blocks for an arbitrary nonnegative shell-energy profile. The present result obtains the same ratio from logarithmically divergent critical **row** Gram matrices, where fixed cross-frequency phases become lower-order. These are different decompositions of the same Jordan energy.

`FD-040` controls fixed finite packets for `beta>1/2` but leaves a packet-dependent frame constant. `FD-042` fills its critical boundary and shows that the limiting constant improves to the universal `delta_ns`. `FD-041` reaches the same constant through a third route: a scalar energy with stable multiplicative index `alpha=1` has powerful-sieve occupation `delta_pow(1)=delta_ns`. Equation (23) explains why a finite critical packet naturally has linear-times-slowly-varying total energy, the scalar regime corresponding to that `alpha=1` member.

These agreements are an internal falsification check: terminal block density, critical finite-packet Gram scalarization, and the powerful-number dilation sieve all produce the same number without sharing the same proof.

## 6. Consequence for the physical source and the remaining escape

For the physical quotient-shell source, `FD-033` gives

\[
\sum_{n\ge1}
\frac{\Delta\mathcal H(n)}{n^s}
=
\frac{\zeta(s+1)}{\zeta(s)}.
\tag{34}
\]

The nontrivial zeros of `zeta` are therefore the natural Mellin singularities of `mathcal H`. `FD-040` already says that a finite isolated dominant packet at any fixed exponent `beta>1/2` cannot make `U/E` vanish. The present result adds the critical endpoint: if, in any regime, the physical source admitted a finite dominant expansion of the form (20), then

\[
\boxed{
\frac{U_{H,D}}{E_{H,D}}
\longrightarrow\delta_{\mathrm{ns}}>0.
}
\tag{35}
\]

This is conditional when applied to `mathcal H`. Hardy's theorem and the actual zeta spectrum do not provide a finite dominant critical packet; infinitely many comparable critical frequencies, growing packet dimension, arbitrarily close frequency differences, or a remainder of the same critical size remain outside (20).

The surviving physical escape is therefore narrower than after `FD-040`: it must defeat not only every fixed supercritical frame but also the universal critical scalarization of every fixed finite packet. A natural next quantitative target is a **growing-packet** version of (9)--(10): control the operator norm of the off-diagonal critical Gram terms relative to `log R`. Any family for which that norm is `o(log R)` would still have occupation ratio `delta_ns+o(1)`. Hence a vanishing physical ratio would require spectral coherence strong enough for the growing off-diagonal Gram to compete with the logarithmic diagonal.

This does not establish such a growing-packet bound and does not prove the accepted joint-occupation clue. It identifies the exact finite-dimensional critical obstruction that any remaining infinite-spectrum mechanism must overcome.

## 7. Prior art and falsification boundary

Finite exponential sums, almost-periodic functions, Abel summation, mean values of multiplicative functions, and Jordan totients are classical. A targeted literature audit around Jordan-totient/squarefree mean values, logarithmic exponential sums, almost-periodic Dirichlet polynomials, and Mellin/regular-variation convolution found those general ingredients but no external theorem needed for (9)--(12) or (23)--(24). No novelty is claimed for the ingredients in isolation, and no new `SOURCES.md` dependency is load-bearing. The Mathia-specific contribution is the critical nonsquarefree Jordan-row comparison and its placement between the finite-packet boundary of `FD-040` and the physical hyperbola-amplification problem.

The finding is falsified if the summatory laws of `FD-038` do not imply bounded off-diagonal critical sums, if a fixed finite `Gamma` gives a non-scalar `log R` leading Gram term, or if an explicit shell profile satisfying (20) has a leading total or nonsquarefree energy different from (23)--(24). It makes no assertion for packet dimension or frequency set varying with `H`, and no conclusion about RH follows from the positive constant alone.