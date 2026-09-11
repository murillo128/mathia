# AF-277 — Unbounded Dirichlet sampling recovers full coefficient breadth

**Status:** `CLASSICAL-IDENTITY`, `LITERATURE+DERIVED`, `EXACT-DERIVED`, `ARITHMETIC-FIDELITY`, `DIRICHLET-UNIQUENESS`, `INFINITE-SAMPLING`, `PRIME-BREADTH`, `STABILITY-WARNING`, `NO-NOVELTY-CLAIM`

## Claim

AF-275 and AF-276 show that every **finite** family of exact values or finite jets in the absolute-convergence half-plane leaves nontrivial far-prime fibers in a degree-one Euler family. There is a sharp positive boundary once the retained value samples themselves escape to the far right.

Let

\[
F(s)=\sum_{n\ge1}a_n n^{-s},
\qquad
G(s)=\sum_{n\ge1}b_n n^{-s}
\tag{1}
\]

be ordinary Dirichlet series that converge absolutely in a common half-plane `Re(s)>sigma_a`. Let `(s_j)` be any sequence with

\[
\operatorname{Re}(s_j)=\sigma_j\longrightarrow+\infty.
\tag{2}
\]

Then:

1. **Exact samples on `(s_j)` are coefficient-faithful.** If
   \[
   F(s_j)=G(s_j)
   \qquad\text{for every }j,
   \tag{3}
   \]
   then
   \[
   a_n=b_n
   \qquad\text{for every }n\ge1.
   \tag{4}
   \]
   This is the classical uniqueness theorem for ordinary Dirichlet series, in exactly the form recorded by Apostol.

2. **The coefficients can be recovered recursively from those escaping samples.** If `c>sigma_a`, then
   \[
   a_1=\lim_{j\to\infty}F(s_j),
   \tag{5}
   \]
   and, once `a_1,\ldots,a_{N-1}` are known,
   \[
   \boxed{
   a_N
   =\lim_{j\to\infty}
   N^{s_j}
   \left(
   F(s_j)-\sum_{n<N}a_n n^{-s_j}
   \right).
   }
   \tag{6}
   \]

3. **The convergence has an explicit tail modulus.** Writing
   \[
   A_{N,c}:=\sum_{n>N}|a_n|n^{-c}<\infty,
   \tag{7}
   \]
   one has, for every `sigma_j>=c`,
   \[
   \left|
   N^{s_j}
   \left(F(s_j)-\sum_{n<N}a_n n^{-s_j}\right)
   -a_N
   \right|
   \le
   N^c A_{N,c}
   \left(\frac{N}{N+1}\right)^{\sigma_j-c}.
   \tag{8}
   \]

4. **Exact fidelity is not uniform numerical fidelity.** If the retained sample is perturbed by `eta_j`, the same coefficient estimator acquires the additional error
   \[
   N^{\sigma_j}|\eta_j|.
   \tag{9}
   \]
   Thus moving farther right exponentially suppresses contamination from coefficients `n>N` but exponentially amplifies absolute sample error. Exact injectivity and stable recovery are separate properties.

5. **For ordinary degree-one Euler products this pays the full prime-breadth bill.** Suppose
   \[
   Z_\alpha(s)
   =\prod_p(1-\alpha_p p^{-s})^{-1}
   =\sum_{n\ge1}f_\alpha(n)n^{-s}
   \tag{10}
   \]
   and similarly `Z_beta`, with both Dirichlet series absolutely convergent in a common right half-plane. Since
   \[
   f_\alpha(p)=\alpha_p,
   \tag{11}
   \]
   equality
   \[
   Z_\alpha(s_j)=Z_\beta(s_j)
   \qquad\forall j,
   \quad \sigma_j\to\infty,
   \tag{12}
   \]
   forces
   \[
   \alpha_p=\beta_p
   \qquad\text{for every rational prime }p.
   \tag{13}
   \]

Therefore the AF-275/276 obstruction is genuinely a **finite-observation** obstruction, not a claim that isolated right-half-plane samples are intrinsically incapable of carrying prime breadth. A countably infinite sampling channel whose real parts escape to infinity is already exact-source faithful in the ordinary Dirichlet-series category, even though the sample set has no finite accumulation point in the analytic domain.

The mechanism is not the ordinary identity theorem. It is the well-ordered exponential scale

\[
1,\ 2^{-s},\ 3^{-s},\ldots
\tag{14}
\]

which lets the least unresolved coefficient dominate as `Re(s)->infinity`.

## Exact derivation and quantitative recovery

Fix `c>sigma_a`. Absolute convergence gives

\[
\sum_{n\ge1}|a_n|n^{-c}<\infty.
\tag{15}
\]

For a fixed `N`, subtract the already recovered prefix and multiply by `N^s`:

\[
N^s
\left(
F(s)-\sum_{n<N}a_n n^{-s}
\right)
=
a_N+
\sum_{n>N}a_n\left(\frac Nn\right)^s.
\tag{16}
\]

For `sigma=Re(s)>=c`, the tail satisfies

\[
\begin{aligned}
\left|
\sum_{n>N}a_n\left(\frac Nn\right)^s
\right|
&\le
\sum_{n>N}|a_n|\left(\frac Nn\right)^\sigma\\
&=
N^c
\sum_{n>N}|a_n|n^{-c}
\left(\frac Nn\right)^{\sigma-c}\\
&\le
N^c A_{N,c}
\left(\frac{N}{N+1}\right)^{\sigma-c}.
\end{aligned}
\tag{17}
\]

The last factor tends to zero as `sigma->infinity`, proving `(6)` and `(8)`. The case `N=1` gives `(5)` directly.

The standard uniqueness theorem follows immediately. If `F(s_j)=G(s_j)` for all `j`, let

\[
H(s)=F(s)-G(s)=\sum_{n\ge1}d_n n^{-s}.
\tag{18}
\]

If the coefficient laws differed, choose the least `N` with `d_N!=0`. Then

\[
0=N^{s_j}H(s_j)
=d_N+
\sum_{n>N}d_n\left(\frac Nn\right)^{s_j}.
\tag{19}
\]

The same bound `(17)` makes the tail tend to zero as `j->infinity`, forcing `d_N=0`, a contradiction. Hence every coefficient agrees.

This proof works for complex sample points as long as their real parts tend to `+infinity`: the phases in `(N/n)^{s_j}` do not matter because their magnitudes are `(N/n)^{sigma_j}`.

## Conditioning: the positive exact result has a severe metric price

Suppose the observed value is

\[
\widetilde F(s_j)=F(s_j)+\eta_j.
\tag{20}
\]

Using the same prefix-subtracted estimator gives

\[
\widehat a_N(j)
:=N^{s_j}
\left(
\widetilde F(s_j)-\sum_{n<N}a_n n^{-s_j}
\right).
\tag{21}
\]

Combining `(8)` with the sample perturbation yields

\[
|\widehat a_N(j)-a_N|
\le
N^cA_{N,c}
\left(\frac{N}{N+1}\right)^{\sigma_j-c}
+
N^{\sigma_j}|\eta_j|.
\tag{22}
\]

The two terms move in opposite directions with `sigma_j`.

- The unknown higher-coefficient tail is suppressed at approximately
  \[
  \exp\!\left(-\frac{\sigma_j-c}{N+1}\right)
  \tag{23}
  \]
  for large `N`.
- Absolute observation error is amplified by
  \[
  \exp(\sigma_j\log N).
  \tag{24}
  \]

So the exact theorem does **not** produce a uniform low-cost encoding of arbitrarily remote coefficients. Recovering increasing coefficient depth from noisy samples requires a precision budget that can grow extremely rapidly. This is the quantitative counterpart of the line's recurring distinction between exact fidelity and stable fidelity.

No optimal noisy sampling theorem is claimed here; `(22)` is only the direct conditioning law for the classical recursive recovery.

## Arithmetic specialization: finite fibers disappear only after observation dimension becomes infinite

AF-275 constructs, for every finite set of real sample points, nontrivial finitely supported prime-local perturbations that match all retained values exactly. AF-276 shows that retaining any finite collection of derivatives at finitely many points still leaves such a fiber.

AF-277 identifies the opposite boundary in the same absolute-convergence regime. If a degree-one Euler perturbation matched `zeta` on a sequence `(s_j)` with `Re(s_j)->infinity`, its Dirichlet coefficients would agree with those of `zeta`; in particular every prime coefficient would equal `1`. Hence the perturbation would be trivial.

The transition is therefore

\[
\boxed{
\text{finite values / finite jets}
\;\Longrightarrow\;
\text{exact prime-breadth fibers},
}
\tag{25}
\]

whereas

\[
\boxed{
\text{values along }\operatorname{Re}(s_j)\to\infty
\;\Longrightarrow\;
\text{full Dirichlet-coefficient fidelity}.
}
\tag{26}
\]

This answers one live breadth question from the current Arithmetic Fidelity state. The missing resource is not necessarily an open set of analytic data or a full germ. In the ordinary Dirichlet-series category, **unbounded acquisition depth itself** is sufficient: each farther-right scale asymptotically peels off the next unresolved coefficient.

At the same time `(22)` prevents overinterpreting this as an efficient compression. The price of using the asymptotic hierarchy as a decoder is severe conditioning, and the number of exact observations needed to identify an unbounded coefficient family is itself unbounded.

## Prior art and novelty assessment

The exact injectivity statement is classical, not new.

Tom M. Apostol, *Introduction to Analytic Number Theory*, Springer, 1976, Chapter 11, §11.3, Theorem 11.3, states precisely that two ordinary Dirichlet series which are absolutely convergent in a common right half-plane and agree on an infinite sequence `s_k` with `Re(s_k)->+infinity` have identical coefficients. DOI: `10.1007/978-1-4757-5579-4`. Springer confirms the book metadata and the Dirichlet-series chapter; the theorem is also reproduced in standard analytic-number-theory course notes derived from Apostol.

The proof above is the classical least-nonzero-coefficient argument, written in the line's fidelity language. Equation `(8)` is the explicit tail estimate already implicit in that proof. Equation `(22)` is the immediate noisy-data consequence of the same estimate.

No novelty is claimed for Dirichlet-series uniqueness, coefficient extraction at `+infinity`, or Euler-product coefficient recovery. The Arithmetic Fidelity contribution is only the **boundary placement relative to AF-275/276** and the explicit separation of exact source injectivity from its conditioning cost:

- finitely many isolated right-half-plane values or finite jets cannot pay infinite prime breadth;
- an unbounded infinite sample sequence can pay it exactly because the Dirichlet basis has an asymptotically ordered scale;
- that exact decoder is badly conditioned under absolute sample noise.

This boundary is source-category specific. It must not be generalized to arbitrary analytic functions, for which a sequence accumulating only at infinity need not determine the function.

## Boundaries and failure modes

- The theorem assumes ordinary Dirichlet-series representations with absolute convergence in a common right half-plane. It is not a uniqueness theorem for arbitrary holomorphic functions.
- The retained sample family is infinite. AF-277 therefore does not rescue any finite-dimensional compression ruled out by AF-275 or AF-276.
- Equality of values is exact. Approximate equality requires a declared coefficient class and error model; `(22)` shows why no free stability statement follows from exact uniqueness.
- The sequence need not have a finite accumulation point. Its decisive property is `Re(s_j)->+infinity` (or merely the existence of such a subsequence).
- The Euler specialization assumes that the local product expands into an ordinary absolutely convergent Dirichlet series and that the prime coefficient is the local degree-one parameter. Extra global axioms such as a functional equation or automorphy are neither needed nor obtained.
- The result recovers coefficients in the index order `1,2,3,...`; it does not provide a computationally efficient or finite-precision reconstruction of an infinite prime law.
- No RH consequence follows. The theorem concerns source recovery in the absolute-convergence half-plane, not the zero set in the critical strip.

## Decisive audit test

For any proposed infinite sampling compression of an Euler/Dirichlet source, first ask whether the sample set contains a sequence whose real parts tend to `+infinity`. If it does, ordinary Dirichlet-series uniqueness already supplies exact coefficient fidelity; do not rediscover that injectivity under new terminology.

The nontrivial residual is quantitative. Audit the source class through a weighted coefficient budget such as `(7)`, specify the sample-noise norm, and estimate the inverse modulus. A proposed stable recovery must beat or structurally bypass the amplification visible in `(22)` rather than merely invoke exact uniqueness.

Conversely, if only finitely many values or finite jets are retained, AF-275/276 remain the relevant obstruction and exact coefficient recovery cannot be inferred from Apostol's theorem.

## Consequence for the research line

The prime-breadth frontier now has both sides of one clean sampling boundary. Finite global analytic summaries leave exact far-prime fibers, while a countably infinite sequence escaping to the far right is already coefficient-faithful by a classical Dirichlet-series theorem.

This narrows the search for a genuinely useful RH-facing compression. Merely replacing a finite sample set by infinitely many exact right-half-plane samples solves identifiability only by paying an infinite observation bill, and the direct inverse is exponentially sensitive to absolute error. A stronger mechanism would need to exploit additional zeta-specific cross-prime structure to obtain either **finite or lower-complexity acquisition with genuine rigidity**, or **an infinite acquisition scheme with a materially better stability modulus** than the raw asymptotic coefficient decoder.