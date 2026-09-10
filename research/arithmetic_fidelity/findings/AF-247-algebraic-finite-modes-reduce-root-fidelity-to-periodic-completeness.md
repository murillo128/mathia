# AF-247 — Algebraic finite modes reduce root fidelity to periodic completeness

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `CLASSICAL-STRUCTURE`, `OUTPUT-SAMPLING`, `RATE-SENSITIVE-OBSERVABILITY`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-246 shows that arbitrary finite unit-circle exponential modes can lose an exponential root rate through exponentially accurate near-zero recurrence, even when exact periodic aliases have been excluded. For the algebraic subclass, that near-zero obstruction disappears: classical number-field growth bounds for nondegenerate linear recurrences force every nonzero term to be only subexponentially small.

Let

\[
F(n)=\sum_{j=1}^m c_j u_j^n,
\qquad c_j,u_j\in\overline{\mathbb Q},
\qquad |u_j|=1,
\tag{1}
\]

with distinct `u_j` and not all `c_j` zero. For an unbounded set `S\subset\mathbb N`, define

\[
\theta_S(F)=\limsup_{\substack{n\to\infty\\n\in S}}|F(n)|^{1/n}.
\tag{2}
\]

Then:

1. there is an integer `q\ge1` such that, on every residue class `r mod q`, either `F(qk+r)` is identically zero or
   \[
   |F(qk+r)|=e^{o(k)}
   \quad\text{in the lower-bound sense}\quad
   \forall\varepsilon>0:\ |F(qk+r)|\ge e^{-\varepsilon k}
   \tag{3}
   \]
   for all sufficiently large `k`;
2. consequently
   \[
   \boxed{\theta_S(F)\in\{0,1\}},
   \tag{4}
   \]
   and `\theta_S(F)=1` exactly when `S` contains infinitely many indices outside the eventual exact zero set of `F`;
3. therefore the following are equivalent for an unbounded `S`:

   **(a)** every nonzero algebraic finite unit-circle mode `(1)` has `\theta_S(F)=1`;

   **(b)** every residue class modulo every positive integer is visited infinitely often by `S`:
   \[
   \boxed{
   \forall q\ge1,\ \forall r\in\mathbb Z/q\mathbb Z,
   \quad |S\cap(r+q\mathbb Z)|=\infty.
   }
   \tag{5}
   \]

Thus **periodic completeness is the exact universal root-observability criterion for algebraic finite modes**. The stronger irrational shrinking-target obstruction of AF-246 is genuinely transcendence-sensitive: it cannot occur with infinitely many nonzero terms when both the phases and coefficients are algebraic.

## Why it matters

AF-245 identified periodic completeness as only a first audit for arbitrary finite modes: visiting every residue class rules out finite-order aliases but says nothing by itself about irrational characters. AF-246 then isolated the missing phenomenon as exponential shrinking toward an analytic zero target.

AF-247 separates those two mechanisms sharply. In the algebraic category, the Subspace-Theorem growth machinery rules out exponential near-cancellation after the root-of-unity degeneracies have been split into residue classes. Hence the full quantitative shrinking-target condition collapses back to a purely profinite one: avoid eventual confinement to a proper periodic subset.

This is a useful fidelity boundary. A sampled root-rate failure with infinitely many nonzero terms is impossible for algebraic finite-mode data, so any such failure necessarily uses transcendental data somewhere in the finite mode. Conversely, the actual Li dominant phases arising from hypothetical off-critical zeta zeros are not known to satisfy the algebraicity assumptions, so this theorem does not turn periodic completeness into an RH criterion. It identifies precisely why AF-246 still needs the larger shrinking-target category for the zeta application.

## Derivation / evidence

### 1. Split all root-of-unity degeneracies into residue classes

Put `i\sim j` when `u_i/u_j` is a root of unity. Choose `q` divisible by the orders of all such ratios. For each equivalence class `C`, choose a representative `v_C`; write

\[
u_j=v_C\zeta_j\qquad(j\in C),\qquad \zeta_j^q=1.
\tag{6}
\]

For a fixed residue `r mod q`,

\[
F(qk+r)
=\sum_C A_{C,r}\,\alpha_C^k,
\qquad
\alpha_C=v_C^q,
\tag{7}
\]

where

\[
A_{C,r}=v_C^r\sum_{j\in C}c_j\zeta_j^r.
\tag{8}
\]

All `A_{C,r}` and `\alpha_C` are algebraic, and `|\alpha_C|=1`. After deleting classes with `A_{C,r}=0`, any two surviving characteristic roots have quotient that is not a root of unity. Hence `(7)` is either identically zero or a nondegenerate algebraic linear recurrence.

### 2. Scale to the classical number-field growth theorem

Fix a residue for which `(7)` is nonzero. Choose an integer `D>1` such that every `D\alpha_C` is an algebraic integer. Then

\[
H_r(k):=D^kF(qk+r)
=\sum_C A_{C,r}(D\alpha_C)^k
\tag{9}
\]

is a nondegenerate linear recurrence over a number field whose characteristic roots are algebraic integers of common complex modulus `D>1`.

The accessible number-field growth theorem proved in the appendix of Fuchs--Heintze states that for such a nondegenerate recurrence, for every `\eta>0`,

\[
|H_r(k)|\ge D^{k(1-\eta)}
\tag{10}
\]

for all sufficiently large `k`. Their proof is based on Evertse's lower bounds for sums of `S`-units together with Schmidt's finiteness theorem for zeros of nondegenerate recurrences.

Dividing `(10)` by `D^k` gives

\[
|F(qk+r)|\ge D^{-\eta k}.
\tag{11}
\]

Because `\eta>0` is arbitrary, for every `\varepsilon>0` one may choose `\eta` small enough that `(11)` implies

\[
|F(qk+r)|\ge e^{-\varepsilon(qk+r)}
\tag{12}
\]

for all sufficiently large `k`. Since `F` is bounded above, every nonzero residue subsequence therefore satisfies

\[
|F(qk+r)|^{1/(qk+r)}\longrightarrow1.
\tag{13}
\]

This proves the first two parts of the claim. It also recovers, in this simple finite-mode setting, the Skolem--Mahler--Lech shape of the zero set: up to finitely many exceptional indices, the zeros are exactly the residue classes for which `(7)` vanishes identically.

### 3. Periodic completeness is sufficient

Assume `(5)`. A nonzero `F` cannot vanish identically on every residue class modulo `q`, since that would make `F(n)=0` for all `n` and contradict the Vandermonde independence of distinct exponentials.

Choose one residue `r mod q` on which `(7)` is nonzero. By `(5)`, `S` contains infinitely many indices in that residue. Along those retained indices `(13)` holds, so

\[
\theta_S(F)=1.
\tag{14}
\]

Thus periodic completeness makes `S` root-observable for every algebraic finite mode.

### 4. Periodic completeness is necessary

Conversely, suppose `(5)` fails. Then for some `q` and residue `r`, the set `S\cap(r+q\mathbb Z)` is finite. Let `\omega=e^{2\pi i/q}` and define the periodic Fourier idempotent

\[
F_r(n)=\frac1q\sum_{j=0}^{q-1}\omega^{j(n-r)}.
\tag{15}
\]

Its coefficients and phases are algebraic, and

\[
F_r(n)=
\begin{cases}
1,&n\equiv r\pmod q,\\
0,&n\not\equiv r\pmod q.
\end{cases}
\tag{16}
\]

Therefore `F_r` is a nonzero algebraic finite mode but is eventually zero on `S`, so `\theta_S(F_r)=0`. Universal algebraic-mode root observability fails. This proves necessity and completes `(a)\iff(b)`.

## AF-246 shrinking-target consequence

For algebraic mode data, AF-246's shrinking exponent has a dichotomy. If `S` contains infinitely many nonzero values of `F`, then `(12)` together with AF-246 gives

\[
\tau_F(S)=0.
\tag{17}
\]

If `F` is eventually zero on `S`, then `\tau_F(S)=+\infty`. Hence no finite positive shrinking exponent survives in the algebraic finite-mode category:

\[
\boxed{\tau_F(S)\in\{0,+\infty\}.}
\tag{18}
\]

The positive finite defects permitted abstractly by AF-246 therefore require leaving this algebraic category.

## Prior-art audit

The recurrence-growth input is classical, not a new theorem of Mathia. Jan-Hendrik Evertse, **“On sums of S-units and linear recurrences,”** *Compositio Mathematica* 53 (1984), 225--244, gives the `S`-unit estimates underlying the number-field theory: https://www.numdam.org/item/CM_1984__53_2_225_0/ .

Clemens Fuchs and Sebastian Heintze, **“On the growth of linear recurrences in function fields,”** *Bulletin of the Australian Mathematical Society* 104 (2021), 11--20, DOI `10.1017/S0004972720001094`, includes in its appendix a complete proof of the number-field statement used above; their Theorem 6 states the `|G_n|\ge (\max|\alpha_j|)^{n(1-\varepsilon)}` lower bound for nondegenerate recurrences with algebraic-integer characteristic roots of maximal modulus greater than one. The paper explicitly traces the proof to Evertse and Schmidt: https://arxiv.org/abs/2006.11074 .

The exact-zero decomposition is the classical Skolem--Mahler--Lech phenomenon. AF-247 does not claim novelty for recurrence growth, `S`-unit lower bounds, or periodic zero sets. The derived contribution here is their insertion into AF-246's root-fidelity framework, yielding the exact equivalence `(5)` for the algebraic finite-mode sampling class and the shrinking-exponent dichotomy `(18)`.

## Boundaries

**Algebraicity is essential to this argument.** The coefficients and phases in `(1)` must lie in a number field. With arbitrary complex data, a dense irrational orbit can be sampled along exponentially accurate shrinking targets, exactly as AF-246 allows. The theorem therefore cannot be applied to hypothetical off-RH Li phases without an independent algebraicity theorem for the relevant mode data.

**This is output sampling, not source compression.** Even a set satisfying `(5)` may contain extremely sparse and very large indices. Computing a retained Li coefficient can still require essentially its original source depth, so AF-238--AF-243's cancellation-coherent source-access obstruction remains untouched.

**Infinite residue visits are the exact condition only for the algebraic finite-mode class.** For arbitrary unit-circle phases, periodic completeness still fails to control irrational shrinking targets. AF-246 remains the correct general criterion.

## Research consequence

The output-sampling hierarchy now has a clean arithmetic split. For unrestricted phase data, universal root fidelity is a quantitative shrinking-target problem. For algebraic finite modes, Subspace-Theorem rigidity removes the near-zero branch and leaves only exact periodic aliasing, characterized by `(5)`.

This suggests that further attempts to weaken Bohr observability should state the coefficient/phase category explicitly. In the full Li problem, the useful next output-side question is no longer simply whether periodic completeness suffices—it does in the algebraic category—but what arithmetic or Diophantine restrictions, if any, are actually available for the zero-derived phase data. The harder independent frontier remains the source side: constructing enough Li information with cancellation-coherent access before the root-rate quotient is formed.