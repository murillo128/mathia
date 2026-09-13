# MC-257 — Shell small primes kill every wild prime-square Sylow direction

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

In the shell-square setup of `MC-238` and `MC-246`, let

\[
S=\{r\text{ prime}: y<r\le 2y\},\qquad
q=\prod_{r\in S}r^2,\qquad
R=\prod_{r\in S}r,
\]

with `y>=2`, and write

\[
G=(\mathbb Z/q\mathbb Z)^\times,
\qquad
H=\langle p\bmod q: p\le y\text{ prime}\rangle.
\]

Let

\[
\pi:G\longrightarrow (\mathbb Z/R\mathbb Z)^\times
\]

be squarefree reduction and

\[
U=\ker\pi=\prod_{r\in S}U_r,
\qquad
U_r=1+r\mathbb Z/r^2\mathbb Z\cong C_r.
\]

Then

\[
\boxed{U\subseteq H.}
\tag{1}
\]

Hence the exact blind quotient has no wild prime-square component:

\[
\boxed{
G/H\text{ is a quotient of }(\mathbb Z/R\mathbb Z)^\times.
}
\tag{2}
\]

Equivalently, every character in the annihilator `H^perp` modulo `q` is trivial on `U` and therefore factors through the squarefree modulus `R`; its primitive conductor divides `R` rather than requiring a square factor from any shell prime.

This closes one of the explicit possibilities left by `MC-256`: the order-`r` wild direction of `(Z/r^2 Z)^times` does **not** survive the actual moving shell. Any remaining blind arithmetic is already contained in the tame squarefree shell quotient.

## 1. Fermat quotients detect the local wild component

For an odd prime `r` and an integer `a` coprime to `r`, define the Fermat quotient

\[
q_r(a)=\frac{a^{r-1}-1}{r}\pmod r.
\tag{3}
\]

The binomial expansion gives the classical homomorphism law

\[
q_r(ab)=q_r(a)+q_r(b)\pmod r.
\tag{4}
\]

On the wild subgroup,

\[
q_r(1+rt)\equiv -t\pmod r,
\tag{5}
\]

so the restriction `q_r:U_r -> F_r` is an isomorphism. Consequently

\[
K_r:=\ker q_r\subseteq(\mathbb Z/r^2\mathbb Z)^\times
\]

has order `r-1`, and `q_r(a) != 0` is exactly the statement that the residue of `a` has a nontrivial wild `r`-primary component.

## 2. Every shell prime sees a nonzero small-prime Fermat quotient

Fix `r in S`. We prove directly that there is a prime `p<=y` with

\[
q_r(p)\ne0.
\tag{6}
\]

Assume first `r>=11` and set

\[
m=\frac{r-1}{2}.
\]

Because `r<=2y`, one has `m<y`. Suppose for contradiction that `q_r(p)=0` for every prime `p<=y`. By `(4)`, every integer `1<=n<=m` then lies in `K_r`.

For `k=1,2,3,4`, define the integer set

\[
A_k=\left\{kn:\ \left\lfloor\frac{(k-1)m}{k}\right\rfloor<n\le m\right\}.
\tag{7}
\]

Here both `k` and `n` are at most `m`, hence both lie in `K_r`; multiplicativity gives `A_k subseteq K_r`. Moreover

\[
A_k\subset ((k-1)m,km],
\]

so the four sets are pairwise disjoint as integers. Their largest element is at most

\[
4m=2(r-1)<r^2,
\]

therefore they remain pairwise distinct as residues modulo `r^2`. Finally,

\[
|A_k|
=m-\left\lfloor\frac{(k-1)m}{k}\right\rfloor
\ge \frac{m}{k},
\]

and hence

\[
\left|\bigcup_{k=1}^4A_k\right|
\ge m\left(1+\frac12+\frac13+\frac14\right)
=\frac{25}{12}m
>2m=r-1.
\tag{8}
\]

This contradicts `|K_r|=r-1`.

The remaining odd primes are immediate with the base `2`:

\[
q_3(2)=1,\qquad q_5(2)=3,\qquad q_7(2)=2\pmod r.
\tag{9}
\]

Thus `(6)` holds for every shell prime when `y>=2`.

## 3. Shell width isolates the global Sylow subgroup

Under the Chinese remainder decomposition,

\[
G\cong\prod_{s\in S}(\mathbb Z/s^2\mathbb Z)^\times.
\]

Fix `r in S`. For any distinct `s in S`, the prime `r` does not divide `s(s-1)`. The only nontrivial case is `s>r`: since `r>y` and `s<=2y<2r`, the divisibility `r | (s-1)` would force `s=r+1`, which is even and greater than `2`, impossible for prime `s`.

Therefore the factor `r` occurs exactly once in `|G|`, and `U_r` is the unique global Sylow-`r` subgroup. Put

\[
N_r=\frac{|G|}{r}.
\tag{10}
\]

Choose the prime `p<=y` from `(6)` and let `h_p=p mod q in H`. Since `N_r` is divisible by every component order away from the wild `r`-part, `h_p^{N_r}` lies in `U_r`. By `(4)`,

\[
q_r(h_p^{N_r})\equiv N_r q_r(p)\not\equiv0\pmod r,
\]

because `gcd(N_r,r)=1`. Thus `h_p^{N_r}` is a nonidentity element of the prime-order group `U_r`, so it generates `U_r`. Hence

\[
U_r\subseteq H.
\tag{11}
\]

Doing this independently for every `r in S` proves `(1)`.

## 4. The blind quotient descends exactly to the squarefree shell

Since `U=ker pi subseteq H`, one has

\[
H=\pi^{-1}(\pi(H)).
\tag{12}
\]

Consequently

\[
G/H\cong (\mathbb Z/R\mathbb Z)^\times/\pi(H).
\tag{13}
\]

and every blind character modulo `q` is inflated from a character modulo `R`. Likewise the exact coset condition underlying the full-annihilator projector of `MC-246` descends from modulus `q` to modulus `R`: for a unit residue `a`,

\[
a\in H\iff \pi(a)\in\pi(H).
\tag{14}
\]

Nonunit residues remain outside both unit subgroups, so no exceptional case is introduced by the descent.

The reduction is structural, not yet analytic. It lowers the natural conductor ceiling for blind characters from the shell-square modulus `q=R^2` to a divisor of `R`, but no previous character-sum or projector estimate may simply be re-read with this smaller conductor without rechecking its exact hypotheses and normalization.

## 5. Prior art and novelty boundary

The Fermat-quotient mechanism is classical and substantially stronger least-nonvanishing results are known. Bourgain, Ford, Konyagin and Shparlinski prove that the least positive integer `a` with `q_r(a) != 0` is at most `(log r)^(463/252+o(1))`, improving earlier `O((log r)^2)` bounds (`MC-S47`). By factorizing such an `a` and using `(4)`, one immediately obtains a prime divisor with nonzero Fermat quotient at no larger scale. Shparlinski directly studies vanishing `q_r(ell)` for prime arguments `ell` and its relation to subfields of `Q(exp(2 pi i/r^2))` (`MC-S48`).

Therefore **no novelty is claimed** for Fermat quotients, their kernels, least nonvanishing bases, or the existence of a small prime with nonzero quotient. The Mathia-specific contribution here is the exact shell consequence: combining that classical local mechanism with the factor-of-two shell geometry isolates every wild Sylow subgroup inside `H`, so the particular blind quotient from `MC-246` loses all prime-square wild directions.

## Boundaries and falsification audit

- The result does not show that `H=G`; a potentially large tame quotient modulo `R` can remain.
- It does not impose rank rigidity on the remaining squarefree residue-character matrix. In particular it does not reverse `MC-256`, whose universality result concerns tame fixed-order data once localization is removed.
- It does not give a bound for `M(X)` or for the rough signed coset sum from `MC-246`.
- The direct proof of `(6)` uses the shell relation `r<=2y`; outside this geometry, use of the classical polylogarithmic least-nonvanishing theorem has a different quantitative interface.
- Any claimed analytic gain from the conductor descent `q -> R` must be re-derived against the exact character-sum theorem being used. The group-theoretic descent alone supplies no cancellation.

The decisive audit test is algebraic and finite: for any finite shell, compute `H` inside `(Z/qZ)^times` and verify that each generator `1+r mod r^2` of the local wild kernel is contained in the projection of `H`. The proof above establishes this exactly, so a counterexample would identify an arithmetic or CRT error rather than a statistical failure.

## Updated frontier

`MC-256` left four possible ways around fixed-order tame universality: moving-shell localization, source coupling, residue order growing with scale, or the wild order-`r` prime-square direction. This finding removes the fourth possibility in the actual shell construction.

The blind quotient is now exactly a **tame squarefree-shell quotient**. The next useful questions are therefore narrower: whether the conductor descent to `R` materially strengthens the available localized character-sum budget, whether the moving shell forces constraints on the tame cross-prime residue matrix that disappear in separated-prime controls, or whether one must abandon annihilator structure and prove cancellation directly on the exact rough Möbius coset.