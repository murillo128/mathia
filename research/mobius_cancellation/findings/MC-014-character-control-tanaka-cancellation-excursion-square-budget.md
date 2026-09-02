# MC-014 — Character control forces quadratic Tanaka cancellation and isolates an excursion-square budget

**Status:** `EXACT-DERIVED`, `DECISIVE-NEGATIVE`, `MATCHED-MULTIPLICATIVE-CONTROL`, `CANDIDATE-NEW-STRUCTURE`, `NO-NOVELTY-CLAIM`.

## Claim

The two Tanaka components isolated in `MC-013` cannot in general be controlled separately at the `N^(3/2+epsilon)` scale, even for a completely multiplicative sequence whose partial sums are uniformly bounded. The real non-circular information must preserve the cancellation between zero-departure local time and signed feedback.

At the same time, regrouping by whole nonzero excursions gives a cancellation-respecting sufficient statistic. For any path

\[
a(n)\in\{-1,0,1\},\qquad S(0)=0,\qquad S(k)=\sum_{n\le k}a(n),
\]

let `I_j=[alpha_j,beta_j]` be the maximal consecutive blocks of indices `k in {0,...,N-1}` on which `S(k) != 0`, and put

\[
ell_j=\beta_j-\alpha_j+1,
\qquad
E_2(N)=\sum_j \ell_j^2.
\tag{1}
\]

Then pathwise

\[
\boxed{
\sum_{k=0}^{N-1}|S(k)|
\le
\frac12\sum_j \ell_j(\ell_j+1)
\le
\frac12\bigl(E_2(N)+N\bigr).
}
\tag{2}
\]

Consequently, for the Möbius path,

\[
E_2(N)\ll_\varepsilon N^{3/2+\varepsilon}
\quad\Longrightarrow\quad
D_M(N)=\frac1N\int_0^N|M(u)|\,du
\ll_\varepsilon N^{1/2+\varepsilon}.
\tag{3}
\]

The statistic `E_2` depends only on the lengths of excursions of the Mertens walk away from zero. It is stronger than merely counting zero visits, but it does not require pointwise control of excursion height. In the abstract path class, (3) is strictly weaker than a pointwise square-root bound: a path may contain a single monotone excursion of length `N^(3/4)` while still having `E_2(N)=N^(3/2)`.

The exact matched control is the nonprincipal real Dirichlet character modulo `3`,

\[
\chi_3(n)=
\begin{cases}
0,&3\mid n,\\
1,&n\equiv1\pmod3,\\
-1,&n\equiv2\pmod3.
\end{cases}
\tag{4}
\]

It is completely multiplicative, and its summatory walk is

\[
S_\chi(k)=
\begin{cases}
1,&k\equiv1\pmod3,\\
0,&k\equiv0,2\pmod3.
\end{cases}
\tag{5}
\]

Hence its mean-absolute summatory statistic is bounded:

\[
D_\chi(N):=\frac1N\sum_{k=0}^{N-1}|S_\chi(k)|=O(1).
\tag{6}
\]

Nevertheless the **individual** triangular Tanaka terms from `MC-013` are quadratic. For `N=3q`, if

\[
L_0^\chi(N)=\sum_{n<N}(N-n)
\mathbf1_{\{S_\chi(n-1)=0\}}\chi_3(n)^2,
\]

and

\[
C_{\rm sgn}^\chi(N)=\sum_{n<N}(N-n)
\operatorname{sgn}(S_\chi(n-1))\chi_3(n),
\]

then exactly

\[
\boxed{
L_0^\chi(3q)=\frac{3q^2+q}{2},
\qquad
C_{\rm sgn}^\chi(3q)=-\frac{3q^2-q}{2}.
}
\tag{7}
\]

Thus

\[
L_0^\chi(3q)+C_{\rm sgn}^\chi(3q)=q
=3q\,D_\chi(3q),
\tag{8}
\]

but

\[
\boxed{
L_0^\chi(3q)+|C_{\rm sgn}^\chi(3q)|=3q^2=\frac{N^2}{3}.
}
\tag{9}
\]

Therefore any strategy that tries to prove the `MC-013` mean-absolute endpoint by separately establishing

\[
L_0(N),\ |C_{\rm sgn}(N)|\ll_\varepsilon N^{3/2+\varepsilon}
\tag{10}
\]

is structurally misaligned with cancellation: (10) fails for every fixed `epsilon<1/2` on a completely multiplicative control with bounded partial sums. The quadratic cancellation between the two terms is not an error to remove; in a strongly cancelling system it can be the dominant mechanism.

## 1. Excursion-square transfer

Fix one nonzero block `I_j=[alpha,beta]` of length `ell`. Maximality gives `S(alpha-1)=0` when `alpha>0`. Since every increment has absolute value at most one,

\[
|S(\alpha+r)|\le r+1
\qquad(0\le r<\ell).
\tag{11}
\]

Therefore its area satisfies

\[
\ell
\le
\sum_{k=\alpha}^{\beta}|S(k)|
\le
1+2+\cdots+\ell
=
\frac{\ell(\ell+1)}2.
\tag{12}
\]

Summing over all maximal nonzero blocks proves (2), because `sum_j ell_j <= N`.

There is also an exact tail representation. If

\[
R_N(r)=\#\{j:\ell_j\ge r\},
\tag{13}
\]

then

\[
\boxed{
E_2(N)=\sum_{r\ge1}(2r-1)R_N(r).
}
\tag{14}
\]

Thus the mean-absolute transfer question can be phrased as a multiscale **zero-return/excursion-tail** problem. A bound of the shape

\[
\sum_{r\ge1} r\,R_N(r)
\ll_\varepsilon N^{3/2+\varepsilon}
\tag{15}
\]

is sufficient for the desired `D_M` scale, up to harmless constants. This retains the pairing between departure and return that the componentwise Tanaka estimate destroys.

## 2. Exact character falsification of componentwise control

For `chi_3`, the summatory path (5) follows immediately from the repeating coefficient block `(1,-1,0)`. Nonzero blocks consist of the single indices `k congruent 1 mod 3`, so for `N=3q`

\[
E_2^\chi(3q)=q.
\tag{16}
\]

The local-time term receives a contribution precisely from departures `n=3j+1`, while signed feedback receives `-1` precisely from the returns `n=3j+2`. Hence

\[
\begin{aligned}
L_0^\chi(3q)
&=\sum_{j=0}^{q-1}\bigl(3q-(3j+1)\bigr)
=\frac{3q^2+q}{2},\\
C_{\rm sgn}^\chi(3q)
&=-\sum_{j=0}^{q-1}\bigl(3q-(3j+2)\bigr)
=-\frac{3q^2-q}{2},
\end{aligned}
\tag{17}
\]

which proves (7)–(9).

This is a stronger falsification than an arbitrary alternating `+1,-1` walk: `chi_3` is a standard completely multiplicative arithmetic function. The obstruction is therefore not caused by abandoning multiplicativity. What the control does abandon is Möbius's exact square-free support and prime-value pattern, so it does not prove that the two components are separately large for Möbius. It proves instead that multiplicativity, excellent global cancellation, and local periodic structure do **not** justify separate componentwise Tanaka bounds.

## 3. Relation to MC-013 and the accepted transfer clue

`MC-013` correctly labels separate control of `C_sgn` and `L_0` as stronger than necessary and notes that negative feedback may offset local time. The character calculation quantifies that warning sharply: the cancellation can remove a full quadratic main term.

This changes the useful interface. The next source-natural statistic should not ask for independent smallness of local time and sign feedback. It should preserve **excursion pairing** or another coupled cancellation mechanism. The second moment `E_2(N)` is the simplest exact such carrier currently available: it controls the total area without ever splitting a completed excursion into a large positive departure term and a large negative return term.

The carrier is still difficult. `E_2(N)` is generated by the zero set of the same summatory process and is not estimated by fixed-shift Chowla, ordinary Halász theory, or the almost-all short-interval theorem merely by definition. Equation (3) is therefore a transfer theorem, not an unconditional advance toward RH.

## Prior art and novelty assessment

Discrete Tanaka/local-time decompositions are classical and already anchored by Fujita (`MC-S21`). Dirichlet characters and their periodic completely multiplicative structure are classical. The excursion decomposition (2) and tail identity (14) are elementary pathwise consequences, and **no novelty claim is made for excursion theory, Dirichlet-character cancellation, or these combinatorial identities in isolation**.

The research contribution recorded here is narrower: the exact `chi_3` control falsifies componentwise use of the `MC-013` Tanaka carrier at the polynomial scale relevant to this line, and it identifies a cancellation-respecting replacement information budget. A targeted literature check around Mertens zero crossings, successive zeros, and excursion lengths found computational cataloguing of the zero set and excursion extrema, but this finding does not infer novelty from the absence of a matching theorem.

## Boundaries and failure modes

This finding does not establish any new unconditional estimate for `M(x)`, prove that Mertens excursion lengths satisfy (3), or validate the recent Pintz endpoint recorded in `MC-009`.

The main boundaries are:

- `E_2(N)` is a sufficient statistic, not a necessary characterization of small mean-absolute area; a long excursion can have low height and therefore much smaller area than the quadratic upper envelope;
- the character control is multiplicative but does not match Möbius's exact support, so it kills generic componentwise arguments rather than every Möbius-specific argument;
- a proof of (3) obtained by first controlling `M(x)` pointwise at RH scale would be circular for the purpose of this line;
- zero-count information alone is insufficient: `E_2` depends on the **distribution of gaps between returns**, not just their total number;
- statistical evidence for short excursion tails is not arithmetic proof, and Brownian return-time heuristics cannot be imported as a deterministic estimate.

A decisive next test is to ask whether existing arithmetic information can control a truncated excursion tail

\[
\sum_{r\le H}rR_N(r)
\]

with a polynomial gain while the long-excursion remainder is handled by an independent input. A matched square-free-supported multiplicative control with small standard local/correlation statistics but large `E_2` would instead show that even the coupled excursion carrier remains beyond those inputs.

## Consequences for the line

The mean-absolute transfer clue is narrowed in a substantive way:

- **killed:** independent polynomial bounds for the two Tanaka components as a generic cancellation mechanism;
- **survives:** coupled excursion-level control;
- **new exact carrier:** the excursion-length second moment `E_2(N)` and its multiscale tail representation (14).

This carrier is strictly more informative than the zero-departure count in `MC-013` while avoiding the quadratic false cost exposed by `chi_3`. The remaining mathematical question is whether Möbius arithmetic supplies any independent theorem strong enough to control that excursion-tail budget.