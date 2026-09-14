# AF-341 — prime layer retains the RH pole discriminator and leading sign complexity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-BRIDGE`, `ARITHMETIC-FIDELITY`, `ZERO-SENSITIVE-SOURCE`, `SOURCE-COMPLEXITY-GATE`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-339 and AF-340 isolate a source-side tension for the centered Mangoldt coefficients: cancelling the main zeta pole while retaining the zero poles produces ordered sign complexity of order `P/log P`. A natural next possibility is to simplify the arithmetic source itself before applying the sign-complexity gate.

The prime-power decomposition gives an exact test of that idea. Define the **prime layer**

\[
a(n):=
\begin{cases}
\log p,& n=p\text{ is prime},\\
0,&\text{otherwise},
\end{cases}
\tag{1}
\]

and the higher-prime-power tail

\[
r(n):=\Lambda(n)-a(n).
\tag{2}
\]

For `Re(s)>1`, write

\[
A(s):=\sum_p (\log p)p^{-s},
\qquad
R(s):=\sum_p\sum_{k\ge2}(\log p)p^{-ks}.
\tag{3}
\]

Then

\[
-\frac{\zeta'(s)}{\zeta(s)}=A(s)+R(s).
\tag{4}
\]

The tail `R` extends holomorphically to

\[
\boxed{\Re(s)>\tfrac12.}
\tag{5}
\]

Consequently `A=-\zeta'/\zeta-R` gives a meromorphic continuation of the prime layer to the same half-plane. It has residue `+1` at `s=1`, and if `rho` is a zeta zero with `Re(rho)>1/2` and multiplicity `m`, then

\[
\boxed{\operatorname*{Res}_{s=\rho}A(s)=-m.}
\tag{6}
\]

Now center only this prime layer against the uniform integer background,

\[
g(n):=a(n)-1,
\qquad n\ge2,
\tag{7}
\]

and let, initially for `Re(s)>1`,

\[
G(s):=\sum_{n\ge2}g(n)n^{-s}
=A(s)-\bigl(\zeta(s)-1\bigr).
\tag{8}
\]

Using `(4)`,

\[
\boxed{
G(s)
=-\frac{\zeta'(s)}{\zeta(s)}-R(s)-\zeta(s)+1.
}
\tag{9}
\]

Thus `G` is meromorphic on `Re(s)>1/2`; the pole at `s=1` cancels, while every zeta zero in that open half-plane remains a pole with residue `-m`. Therefore

\[
\boxed{
\mathrm{RH}
\iff
G\text{ is holomorphic on }\Re(s)>\tfrac12.
}
\tag{10}
\]

So the higher prime powers are **not needed for this RH-falsification discriminator**: removing all powers `p^k`, `k>=2`, preserves exactly the pole test for zeros to the right of the critical line.

But this fidelity-preserving simplification does not buy the source regularity needed by AF-216. For every integer interval `[L,U]` with `3<=L<U`,

\[
\boxed{
V(g_L,\ldots,g_U)
=2\bigl(\pi(U)-\pi(L-1)\bigr)
-\mathbf 1_{\{L\text{ prime}\}}
-\mathbf 1_{\{U\text{ prime}\}}.
}
\tag{11}
\]

Hence for each fixed `B>1`,

\[
\boxed{
V(g_P,\ldots,g_{\lfloor BP\rfloor})
=\bigl(2(B-1)+o(1)\bigr)\frac{P}{\log P}.
}
\tag{12}
\]

The complementary tail has the opposite resource profile: `r(n)>=0`, so after zero coefficients are deleted its ordered sign variation is zero, while its transform `R` is holomorphic on `Re(s)>1/2` and therefore carries **none of the zeta-zero pole discriminator in that half-plane**.

This gives a sharp layer dichotomy:

\[
\boxed{
\begin{array}{c|c|c}
\text{source layer} & \text{RH-right-half-plane pole fidelity} & \text{ordered sign complexity}\\
\hline
\text{prime layer, centered} & \text{retained} & \Theta(P/\log P)\\
\text{higher prime powers} & \text{absent as poles} & 0
\end{array}}
\tag{13}
\]

In this canonical exponent-layer decomposition, the same first prime layer carries both the RH-relevant pole discriminator and the full leading source-oscillation burden.

## Derivation

### 1. Higher prime powers are holomorphic past the RH boundary

Fix any `sigma_0>1/2`. On the closed half-plane `Re(s)>=sigma_0`,

\[
\sum_p\sum_{k\ge2}(\log p)|p^{-ks}|
\le
\sum_p (\log p)\frac{p^{-2\sigma_0}}{1-p^{-\sigma_0}}.
\tag{14}
\]

Since

\[
1-p^{-\sigma_0}\ge1-2^{-\sigma_0}>0,
\]

we obtain

\[
\sum_p\sum_{k\ge2}(\log p)|p^{-ks}|
\le
\frac{1}{1-2^{-\sigma_0}}
\sum_{n\ge2}(\log n)n^{-2\sigma_0}<\infty.
\tag{15}
\]

Thus the series defining `R` converges absolutely and locally uniformly on `Re(s)>1/2`, proving `(5)`.

Equation `(4)` holds in `Re(s)>1` by the Euler product/logarithmic-derivative expansion. Subtracting the holomorphic `R` then continues `A` meromorphically to `Re(s)>1/2`.

### 2. Centering the prime layer removes the main pole but not zero poles

Near `s=1`,

\[
-\frac{\zeta'(s)}{\zeta(s)}
=\frac1{s-1}+O(1),
\qquad
\zeta(s)=\frac1{s-1}+O(1),
\tag{16}
\]

while `R` is holomorphic there. The principal parts in `(9)` therefore cancel exactly.

If `rho` is a zero of multiplicity `m` with `Re(rho)>1/2`, then locally

\[
-\frac{\zeta'(s)}{\zeta(s)}
=-\frac{m}{s-\rho}+O(1),
\tag{17}
\]

while both `R` and `zeta` are holomorphic at `rho`. Hence `G` has a pole of residue `-m` there.

It follows that `G` is holomorphic throughout `Re(s)>1/2` exactly when `zeta` has no zero in that half-plane. By the functional-equation symmetry `rho -> 1-rho`, absence of zeros to the right of `1/2` is equivalent to all nontrivial zeros lying on the critical line. This proves `(10)`.

### 3. The prime layer alone already spends prime-scale sign variation

For every `n>=3`,

\[
g(n)>0\iff n\text{ is prime},
\tag{18}
\]

because `log p>1` for every prime `p>=3`, while every composite integer has `a(n)=0` and therefore coefficient `-1`.

Every prime in `[L,U]` is odd. Its neighboring integers are even and composite, so their coefficients are negative. Consequently every interior prime contributes exactly two sign-changing edges, while a prime at either endpoint contributes only its one interior edge. No sign-changing edge is counted twice. This proves `(11)`.

Applying the prime number theorem on the fixed multiplicative interval `[P,BP]` gives

\[
\pi(BP)-\pi(P)
=\bigl(B-1+o(1)\bigr)\frac{P}{\log P},
\tag{19}
\]

and `(12)` follows.

Comparing with AF-339 is decisive: including all prime powers changes the exact positive-site set from primes to odd prime powers, but higher prime powers contribute only a lower-order number of sites. The ordinary prime layer already accounts for the full leading `P/log P` sign budget.

### 4. Finite prime-power heads give a fidelity-depth hierarchy

The same argument has a useful generalization. For an integer `K>=1`, define

\[
A_{\le K}(s)
:=\sum_p\sum_{1\le k\le K}(\log p)p^{-ks},
\qquad
R_{>K}(s)
:=\sum_p\sum_{k\ge K+1}(\log p)p^{-ks}.
\tag{20}
\]

Then

\[
-\frac{\zeta'}{\zeta}=A_{\le K}+R_{>K}
\tag{21}
\]

in `Re(s)>1`, and exactly as above

\[
\boxed{
R_{>K}\text{ is holomorphic on }\Re(s)>\frac1{K+1}.
}
\tag{22}
\]

Thus the first `K` prime-power layers carry every logarithmic-derivative zero pole in that larger half-plane. Increasing `K` buys deeper analytic reach, but the source-side leading oscillation after uniform centering does not improve: ordinary primes remain positive isolated sites and already force `Theta(P/log P)` sign variation on fixed multiplicative windows; the added higher powers contribute only lower-order corrections.

At the RH boundary, `K=1` is already enough. This is the sharp reason the first layer is the relevant one for `(10)`.

## Relation to AF-339 and AF-340

AF-340 leaves open a structured nonconstant recoding: perhaps one can quarantine part of the Mangoldt source, simplify the residual source geometry, and keep the useful zero discriminator. The prime-power split is the most canonical first test because it removes an entire arithmetic layer without arbitrary tuning.

The test succeeds on fidelity but fails on complexity. Removing all higher prime powers changes the continuation only by a function holomorphic on `Re(s)>1/2`, so the RH-right-half-plane pole discriminator survives exactly. Yet `(11)`--`(12)` show that the leading source oscillation survives with it. Conversely the discarded higher-power tail is one-signed but has no zero poles in that half-plane.

Therefore the prime-power tail cannot be blamed for AF-339's source-complexity obstruction. The obstruction is already present in the first prime layer itself.

This materially narrows the live recoding route. A successful source simplification cannot merely discard, aggregate, or move the higher prime powers into a harmless background while leaving the prime layer unchanged. It must simplify **within or across the prime layer** while proving that the right-half-plane zero information remains recoverable, or replace ordered sign variation by a different source-complexity notion.

## Exact controls and boundaries

### The retained discriminator is specifically the pole test

The statement about `R` is not that higher prime powers contain no information about primes or zeros in an absolute sense. They are determined by the same prime system. The exact claim is narrower: `R` is holomorphic on `Re(s)>1/2`, so it cannot carry the logarithmic-derivative **pole discriminator** for a zero with real part greater than `1/2`.

### Holomorphy is required only in the open half-plane

No assertion is made about boundary regularity on `Re(s)=1/2`. The higher-power tail reaches that boundary naturally through its `k=2` layer, and the proof only gives holomorphy strictly to the right.

### This does not repair the AF-216 / AF-338 route

Equation `(12)` is still a growing source-order obstruction. As in AF-339 and AF-340, it cannot be substituted into AF-338's fixed-order sufficient theorem to infer a necessary sampling depth growing like `P/log P`. No such joint growing-order theorem has been proved.

### The decomposition is canonical but not uniquely privileged

Exponent layers are intrinsic to the Euler logarithmic derivative, but another transform, grouping, cumulative representation, wavelet-like recoding, or nonlocal lift may mix layers and have different source complexity. AF-341 rules out only the hope that the higher prime powers themselves are the source of the leading oscillatory cost.

### Prime-layer RH sensitivity is classical

The partial sums of `(7)` satisfy

\[
\sum_{2\le n\le x}g(n)
=\vartheta(x)-x+O(1),
\tag{23}
\]

where `vartheta(x)=sum_{p<=x}log p` is Chebyshev's first function. The classical equivalence between RH and square-root-scale control of `vartheta(x)-x` is another expression of the same fact that the prime layer by itself retains the RH discriminator. Equation `(10)` should therefore not be read as a new RH criterion.

## Prior art and novelty assessment

No novelty claim is made for the constituent analytic number theory.

- Titchmarsh, *The Theory of the Riemann Zeta-function*, 2nd ed., is a standard reference for the Euler product, the logarithmic derivative, zero symmetry, and RH-equivalent error estimates for Chebyshev functions.
- The *Encyclopedia of Mathematics* entries **“Mangoldt function”** and **“Chebyshev function”** record the classical identities `psi(x)=sum_{n<=x}Lambda(n)` and `psi(x)=vartheta(x)+vartheta(x^{1/2})+vartheta(x^{1/3})+...`, which is the summatory analogue of the prime-power layer split used here.
- The prime-only Dirichlet series `A(s)=sum_p (log p)p^{-s}` is `-P'(s)` for the classical prime zeta function `P(s)=sum_p p^{-s}`. Prime-zeta continuation and its relation to `zeta` are classical; the half-plane argument above is included directly because the needed statement reduces to the elementary absolute convergence of the `k>=2` tail.

The durable Arithmetic Fidelity contribution is the resource accounting against AF-339/AF-340: **a canonical compression can delete every higher prime-power layer without losing the RH-right-half-plane pole discriminator, but that compression leaves the full leading ordered-sign burden intact.** The sign-simple discarded tail is exactly the part that is analytically too regular to carry that pole discriminator.

## Consequence for Arithmetic Fidelity

The nonconstant-background route is now more constrained. The first natural structured simplification of the Mangoldt source has already separated the resources as cleanly as possible:

\[
\text{higher powers}\;\longrightarrow\;\text{sign-simple but RH-pole-invisible on }\Re(s)>1/2,
\]

while

\[
\text{prime layer}\;\longrightarrow\;\text{RH-pole-faithful but }\Theta(P/\log P)\text{ sign complexity}.
\]

So merely stripping arithmetic harmonics cannot solve the source-side bottleneck. The next useful theorem should test a transform that genuinely reduces the effective complexity **of the prime layer itself** while retaining a recoverable right-half-plane zero discriminator, or prove that a broader class of such transforms cannot do so.