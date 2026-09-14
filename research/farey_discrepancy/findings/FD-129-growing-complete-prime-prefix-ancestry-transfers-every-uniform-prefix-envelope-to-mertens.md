# FD-129 — growing complete prime-prefix ancestry transfers every uniform prefix envelope to Mertens

**Status:** `EXACT-DERIVED + SCALE-DEPENDENT-SOURCES + COMPLETE-PRIME-PREFIX-ANCESTRY + UNIFORM-ENVELOPE-TRANSFER + MERTENS-RECOVERY + RH-CRITERION + NEGATIVE/ROUTE-RESTRICTION`.

`FD-128` leaves the active-scale breadth question open after showing that even infinitely many exact Möbius prime directions can coexist with a square-root common-source envelope and sparse-horizon Fourier-skeleton saturation when the enforced prime set is sufficiently sparse. A natural strengthening is to replace that sparse set by the **complete prime prefix** `p<=Y_H`, let `Y_H->infinity`, and ask whether a horizon-dependent matched control can still keep an RH-scale source envelope while approaching the Fourier equality ray.

There is an exact information barrier before any Fourier estimate is attempted. `FD-029` proves that complete prime-prefix ancestry through `Y` forces the cumulative source to equal the physical Mertens function at every argument `x<=Y`. The important quantifier consequence is that allowing a **different synthetic source at every horizon does not evade this recovery once the source estimate is uniform across horizons**.

Let `B:N->[0,infinity)` be any deterministic envelope. The following are equivalent.

1. The physical Mertens function satisfies

\[
|M(x)|\le B(x)
\qquad(x\ge1).
\tag{1}
\]

2. There exist integers `H_j>=Y_j>=1` with `Y_j->infinity` and, for every `j`, coefficients `a_n^(j)` through `H_j` satisfying

\[
a_1^{(j)}=1,
\qquad
a_n^{(j)}=0\quad(n\text{ nonsquarefree}),
\qquad
a_n^{(j)}\in\{-1,+1\}\quad(n\text{ squarefree}),
\tag{2}
\]

and the complete prime-prefix ancestry law

\[
\boxed{
a_{pn}^{(j)}=-a_n^{(j)}
\quad
(p\le Y_j\text{ prime},\ p\nmid n,\ pn\le H_j),
}
\tag{3}
\]

such that, with

\[
A_j(x):=\sum_{n\le x}a_n^{(j)},
\tag{4}
\]

one has the **uniform prefix envelope**

\[
\boxed{
|A_j(x)|\le B(x)
\qquad(1\le x\le Y_j)
}
\tag{5}
\]

for every `j`.

3. The same statement holds with the stronger requirement

\[
|A_j(x)|\le B(x)
\qquad(1\le x\le H_j).
\tag{6}
\]

Thus a growing complete-prime-prefix matched-control family with a horizon-uniform pointwise envelope exists **if and only if the physical Mertens function already satisfies that envelope**. The sources may depend arbitrarily on `j`; no common-source coherence is required.

In particular, the classical Littlewood criterion gives the exact critical consequence

\[
\boxed{
\mathrm{RH}
\iff
\forall\varepsilon>0\;\exists C_\varepsilon<\infty
\text{ and a family satisfying (2)--(3) with }
|A_j(x)|\le C_\varepsilon x^{1/2+\varepsilon}
\text{ on }x\le Y_j,
}
\tag{7}
\]

where `C_epsilon` is independent of `j`. Requiring the bound on the whole interval `x<=H_j` is equivalent as well. Hence **complete growing ancestry plus a uniform RH-scale source envelope is not a synthetic relaxation of the physical target**. It is already an RH-equivalent control condition.

This does not say that prime ancestry itself proves RH, and it does not rule out useful finite-scale coercivity from broad ancestry. It identifies a specific matched-control design that becomes circular at the critical envelope: the exact initial-prime coverage reconstructs the physical low prefix, while horizon-uniform source control imports the desired Mertens estimate on that reconstructed prefix.

## 1. Finite-scale recovery is independent of the synthetic rough core

Fix one stage `(H,Y)` satisfying (2)--(3). Every squarefree `n<=H` factors uniquely as

\[
n=qr,
\tag{8}
\]

where every prime divisor of `q` is at most `Y` and every prime divisor of `r` is greater than `Y`. `FD-029` proves the exact parametrization

\[
a_{qr}=\mu(q)b_r,
\tag{9}
\]

with arbitrary signs on the `Y`-rough squarefree cores `r`.

If `n<=Y`, no nontrivial rough core can occur: every prime divisor of `n` is at most `n<=Y`. Hence `r=1`, `q=n`, and

\[
\boxed{a_n=\mu(n)\qquad(1\le n\le Y).}
\tag{10}
\]

The nonsquarefree case is already zero on both sides. Summing (10) gives the exact prefix identity

\[
\boxed{A(x)=M(x)\qquad(1\le x\le Y).}
\tag{11}
\]

No common source, asymptotic estimate, prime number theorem, or Fourier argument enters this step. All synthetic freedom lives strictly above the enforced prime cutoff.

## 2. Quantifier transfer defeats horizon-dependent matched controls

Assume a family in statement 2. Fix an arbitrary integer `x>=1`. Since `Y_j->infinity`, choose `j` with `Y_j>=x`. Applying (11) at that stage gives

\[
M(x)=A_j(x).
\tag{12}
\]

The uniform envelope (5) therefore yields

\[
|M(x)|=|A_j(x)|\le B(x).
\tag{13}
\]

Since `x` was arbitrary, statement 1 follows. This argument never compares `a^(j)` with `a^(k)` for different stages. The scale-dependent sources can be mutually incompatible; the growing exact prime prefix still pins down whichever finite piece of the physical source is needed to test a fixed `x`.

Conversely, if statement 1 holds, take

\[
a_n^{(j)}:=\mu(n)
\qquad(1\le n\le H_j)
\tag{14}
\]

for any sequences `H_j>=Y_j->infinity`. The physical Möbius coefficients satisfy (2)--(3), and their cumulative sums satisfy (6). Hence 1 implies 3, while 3 trivially implies 2. This proves the equivalence.

The same proof shows the exact failure mode if the constants are allowed to drift with the stage. Bounds

\[
|A_j(x)|\le C_j B(x)
\tag{15}
\]

with unbounded `C_j` transfer only the vacuous stage-dependent statement `|M(x)|<=C_jB(x)` after choosing a stage containing `x`. **Uniformity in the horizon index is the load-bearing resource.**

## 3. The RH-scale matched-control threshold is exact

Apply the equivalence with

\[
B_\varepsilon(x)=C_\varepsilon x^{1/2+\varepsilon}.
\tag{16}
\]

If, for every `epsilon>0`, such complete-prefix families exist with constants `C_epsilon` independent of the stage, Section 2 gives

\[
M(x)=O_\varepsilon(x^{1/2+\varepsilon})
\tag{17}
\]

for every `epsilon>0`. The classical Littlewood criterion then gives RH. Conversely, under RH the same criterion supplies (17), and the physical choice (14) supplies the required matched-control family. This proves (7).

Only the prefix `x<=Y_j` needs the critical envelope. Requiring a global square-root-plus envelope through all of `H_j` is therefore stronger than necessary for the recovery. Likewise, no endpoint estimate such as `|A_j(H_j)|<<sqrt(H_j)` can replace (5): the endpoint lies outside the forced physical prefix when `Y_j<H_j`, so endpoint-only control does not transfer to `M(x)` at arbitrary fixed `x`.

This separates the present obstruction sharply from `FD-128`. There the enforced infinite set `S` deliberately omits most prime directions, so even very large `x` can contain `S`-free squarefree cores and the identity (11) never expands to all integers. Its square-root envelope is therefore a genuine synthetic control. Complete initial-prime coverage is qualitatively different once the envelope is required uniformly on the recovered prefix.

## 4. Stress tests, prior art, and research consequence

The quantifiers were stress-tested against the natural escape routes. A different source at every horizon does not help, because one stage with `Y_j>=x` already fixes the chosen finite prefix. The result fails if `Y_j` does not tend to infinity, if the ancestry sets omit primes rather than contain every prime below the cutoff, if the ancestry equations are only approximate, or if the source estimate is imposed only above `Y_j`. It also gives no conclusion from a stage-dependent envelope constant and no conclusion from terminal amplitudes alone.

A finite direct check was run on random rough-core assignments: for multiple cutoffs `Y` the resulting exact prime-prefix sources agreed identically with `mu` and `M` throughout `1<=x<=Y`, while differing freely above the cutoff. This is only a regression check; equations (8)--(13) are the proof.

The external prior-art boundary remains classical. The equivalence `RH iff M(x)=O_epsilon(x^(1/2+epsilon))` is already anchored in `SOURCES.md` through Titchmarsh--Heath-Brown, Section 14.25. Work on squarefree-supported Möbius-like multiplicative functions, including Aymone's examples with small partial sums, confirms that small summatory behavior for other sign laws is a genuine neighboring subject, but it does not supply the complete-prefix quantifier transfer above. A targeted search found no additional theorem needed for this finite recovery argument. No novelty is claimed for unique factorization, Möbius multiplicativity, or the Littlewood criterion, so `SOURCES.md` requires no new dependency.

The research consequence is a route restriction for the active scale-breadth program. `FD-030` could combine arbitrarily deep sublinear complete prime ancestry with GCD-duality saturation because its horizon-dependent controls deliberately lacked a uniform critical source envelope. `FD-128` could combine a critical envelope with infinitely many exact prime directions because those directions were sparse rather than a growing complete prefix. **Imposing both missing ingredients at once is no longer an independent control: at RH scale it is equivalent to the physical Mertens target itself.**

Future coercivity tests therefore have to avoid this recovered-prefix circularity. Viable hypotheses include approximate or aggregate prime breadth that does not determine every coefficient below a growing cutoff, source control restricted to the genuinely free region above the cutoff, or a direct Fourier-skeleton energy estimate whose assumptions do not already imply the desired Mertens envelope. The theorem does not choose among those routes and does not prove a new Franel--Landau bound; it removes one apparently stronger matched-control program by identifying exactly where the target estimate re-enters.