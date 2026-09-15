# FD-145 — Rank-truncated ancestry defects have an exact component-orientation gauge

- **Date:** 2026-09-15
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** main-track exact no-go theorem / anchor-connectivity obstruction
- **Depends on:** FD-135, FD-139, FD-143, FD-144

## Claim

FD-144 proves that an arbitrary source-independent family of local ancestry tests can still miss one common source whenever its total observation budget is `o(r_T)`, where every observed squarefree parent has at least `r_T` prime factors. That leaves open whether a sufficiently large number of local tests might recover coefficient orientation once the budget reaches the rank scale.

For **ancestry-defect-only observations on a rank-truncated domain**, test count is not the first obstruction. There is an exact `Z_2` component-orientation gauge.

Fix an integer `R_0 >= 1` and define a bounded source with the same squarefree support as Möbius by

\[
a_n=0\qquad (\mu(n)=0),
\tag{1}
\]

and, for squarefree `n`,

\[
a_n=\mu(n)b(n),
\qquad
b(n)=
\begin{cases}
+1,&\omega(n)\le R_0,\\
-1,&\omega(n)>R_0.
\end{cases}
\tag{2}
\]

Then for every prime `p` and every squarefree parent `n` with `p\nmid n`,

\[
a_{pn}+a_n
=
\mu(n)\bigl(b(n)-b(pn)\bigr).
\tag{3}
\]

Consequently

\[
|a_{pn}+a_n|
=
\begin{cases}
2,&\omega(n)=R_0,\\
0,&\omega(n)\ne R_0.
\end{cases}
\tag{4}
\]

In particular, on **every** ancestry edge whose parent satisfies

\[
\omega(n)>R_0,
\tag{5}
\]

the raw signed defect itself vanishes exactly:

\[
\boxed{a_{pn}+a_n=0.}
\tag{6}
\]

Thus if an observation scheme eventually uses only squarefree parents with

\[
\omega(n)\ge r_T,
\qquad r_T\to\infty,
\tag{7}
\]

then for all sufficiently large `T`, once `r_T>R_0`, **every local ancestry defect visible to the scheme is identically zero**. This remains true for arbitrarily many tests, arbitrary cells, arbitrary source-independent weights, and even arbitrary signed linear functionals of those visible defects.

At the same time, every observed parent is maximally misoriented relative to Möbius:

\[
\boxed{a_n=-\mu(n)}
\qquad
(\mu^2(n)=1,\ \omega(n)\ge r_T>R_0).
\tag{8}
\]

Hence no amount of ancestry-defect-only resolution confined to the high-rank region can recover the absolute Möbius orientation. The missing resource is **connectivity to an anchored component**, not test count.

## 1. Exact edge identity

Let `n` be squarefree and let `p\nmid n`. Since

\[
\mu(pn)=-\mu(n),
\tag{9}
\]

we have

\[
\begin{aligned}
a_{pn}+a_n
&=\mu(pn)b(pn)+\mu(n)b(n)\\
&=-\mu(n)b(pn)+\mu(n)b(n)\\
&=\mu(n)\bigl(b(n)-b(pn)\bigr).
\end{aligned}
\tag{10}
\]

Multiplication by one new prime raises `omega` by exactly one. Therefore there are only three cases.

If `omega(n)<R_0`, then both `n` and `pn` lie in the `b=+1` region, so (10) is zero. If `omega(n)=R_0`, the edge crosses the sign wall and

\[
b(n)-b(pn)=1-(-1)=2,
\tag{11}
\]

so the defect has magnitude `2`. If `omega(n)>R_0`, then both endpoints lie in the `b=-1` region, and (10) again vanishes.

Thus **all nonzero ancestry defects of the source are concentrated on the single rank interface**

\[
\omega(n)=R_0
\quad\longrightarrow\quad
\omega(pn)=R_0+1.
\tag{12}
\]

Nothing probabilistic or asymptotic is used here.

## 2. Arbitrarily large high-rank observation families are blind

Consider any horizon-dependent family of visible squarefree ancestry edges

\[
E_T\subseteq
\{(n,pn):\mu^2(n)=1,\ p\nmid n\}
\tag{13}
\]

such that every visible parent satisfies `omega(n)>=r_T`, with `r_T->infinity`. No restriction is imposed on the number of visible primes, the number of edges, or the number and shape of statistics formed from them.

For all sufficiently large `T`, `r_T>R_0`. By (6),

\[
\boxed{
(a_{pn}+a_n)_{(n,pn)\in E_T}=0
}
\tag{14}
\]

as an entire vector.

Therefore every observable of the form

\[
\Phi_T\bigl((a_{pn}+a_n)_{(n,pn)\in E_T}\bigr)
\tag{15}
\]

has exactly the same value as it would for the Möbius source whenever `Phi_T` depends only on those edge defects and is normalized so that it sees the zero vector as zero. In particular this covers all the nonnegative weighted moments used in FD-138--FD-144, but it is stronger: because the raw vector itself is zero, signed weights, overlapping tests, infinitely fine partitions, and an arbitrarily large test budget do not help.

Yet on the same visible parent set,

\[
a_n=-\mu(n)
\tag{16}
\]

for every squarefree `n`. Thus any direct coefficient observation distinguishes the two sources immediately. The failure belongs specifically to **relative ancestry information without an anchor**, not to the coefficients themselves.

## 3. Graph form: ancestry defects are relative orientation measurements

The exact mechanism is clearer after quotienting out Möbius. On squarefree integers define

\[
b(n):=\frac{a_n}{\mu(n)}\in\{\pm1\}.
\tag{17}
\]

For an ancestry edge `n -> pn`, (10) says

\[
a_{pn}+a_n=0
\quad\Longleftrightarrow\quad
b(pn)=b(n).
\tag{18}
\]

Hence a zero ancestry defect says that the two endpoint orientations agree. A connected collection of such relations can determine `b` **relative to one chosen vertex**, but not its absolute sign. Replacing

\[
b(v)\mapsto-b(v)
\tag{19}
\]

simultaneously on a connected component preserves every equality relation internal to that component.

The finite Möbius-compatible seed supplies an anchor on the low-rank side. The source (2) keeps that anchored component at orientation `+1` and flips the entire high-rank region to `-1`. The only edges capable of communicating the orientation change are precisely the bridge edges (12). Once an observation scheme discards those bridges and looks only above rank `R_0`, it sees a component whose internal ancestry equations are perfectly satisfied but whose absolute orientation is wrong.

This gives the structural form of the obstruction:

> **Relative ancestry constraints recover absolute coefficient orientation only on components connected to an anchored coefficient.**

Counting more tests inside an already disconnected component cannot repair the missing connection.

## 4. Finite-seed compatibility

Suppose the research line fixes finitely many squarefree coefficients to their Möbius values, as in the finite-anchor conventions used by the previous common-source controls. Choose `R_0` larger than the maximum `omega(n)` among those prescribed squarefree integers. Then (2) agrees exactly with the entire finite seed.

The construction is therefore one fixed infinite source, not a horizon-dependent family. After `r_T>R_0`, the same source defeats every high-rank ancestry-defect-only observation horizon simultaneously; no sparse subsequence or probabilistic extraction is required.

This is strictly stronger in that sense than FD-143 and FD-144. Their common sources required probabilistic selection and a subsequence to make a growing collection of tests simultaneously small. Here the visible defects are eventually **exactly zero at every horizon**.

## 5. Relation to FD-144: the linear-rank threshold is conditional

FD-144 establishes a genuine lower bound for broad local test families:

\[
L_T=o(r_T)
\tag{20}
\]

can be defeated even when the tests range over arbitrary source-independent normalized weights. It was natural to ask whether `Theta(r_T)` observations might be a sharp threshold.

FD-145 shows that this threshold question is meaningful only after imposing an anchor-connectivity condition. If all tested edges live above a diverging minimum rank, then even

\[
L_T\gg r_T,
\qquad
L_T\to\infty
\tag{21}
\]

or complete observation of **every** available high-rank ancestry edge does not distinguish the rank-flipped source (2) from Möbius through the edge defects.

Thus there are two logically distinct resources:

1. **orientation connectivity**: does the measured ancestry graph connect the observed region to a coefficient whose Möbius orientation is fixed?
2. **resolution inside the connected region**: once such connectivity is present, how many source-independent observations are required to force coefficient recovery?

FD-144 addresses the second resource. FD-145 proves that the first cannot be omitted.

## 6. Why this does not contradict pointwise ancestry rigidity

The construction does **not** defeat a pointwise `L^infty` ancestry condition imposed on all relevant ranks. At the interface `omega(n)=R_0`, every crossing edge has

\[
|a_{pn}+a_n|=2.
\tag{22}
\]

So any observable that includes even one such bridge with pointwise sensitivity detects the source at full strength. This is exactly compatible with the pointwise-rigidity lesson of FD-135: a sign change cannot be globally hidden if the observation actually crosses it.

The new obstruction comes from rank truncation. Once the measured domain begins strictly above the bridge, all remaining local equations are satisfied exactly. The source has not made the defect small; the observation graph has stopped asking the equation that carries the absolute orientation.

## 7. Matched controls and limits

The result is deliberately narrow about what it rules out.

### 7.1 Direct coefficient samples defeat the source

If an observer is allowed to inspect any high-rank coefficient `a_n` itself, then (16) exposes the flip immediately. FD-145 concerns ancestry-defect-only data.

### 7.2 Anchor-crossing edges defeat the source

If the observation family includes a path of ancestry edges from a seeded Möbius coefficient through the rank interface, then the component orientation is fixed. In particular any edge with parent rank exactly `R_0` has defect magnitude `2` under (2).

### 7.3 Global Fourier or quadratic observables are not covered

A Farey/Franel/Fourier observable may couple coefficients that are not adjacent in the ancestry graph and can therefore be sensitive to absolute orientation even when local defects vanish. FD-145 does not provide a no-go theorem for such observables.

### 7.4 Nonzero signed edge data have more information than magnitudes

The component-gauge interpretation should not be overextended to arbitrary nonzero signed differences. Our exact source avoids this issue: every visible high-rank raw defect is zero. Therefore even signed linear functionals of the visible defect vector vanish. The theorem does not claim a sign-flip invariance for arbitrary nonzero edge measurements.

### 7.5 The rank wall is intentionally simple

The construction does not claim to model a natural arithmetic source. It is a matched control against an inference principle: if the proposed coercive law uses only high-rank ancestry defects, then those data alone cannot distinguish a globally wrong component orientation from the anchored Möbius orientation.

## 8. Prior-art audit

The abstract graph phenomenon is standard. Synchronization over `Z_2` and related group-synchronization problems recover vertex labels from pairwise relative measurements; an unanchored connected component carries a global group-action ambiguity. Modern `Z_2` synchronization literature formulates the data as relative products `R_ij approx z_i z_j`, and anchored versus anchor-free synchronization is a standard distinction.

Therefore **the component/global sign gauge is not claimed as new graph theory**. The Mathia-specific content is the exact splice with the Möbius ancestry identity (10): a single finite rank wall produces one fixed seed-compatible source for which every defect above the wall vanishes identically while every high-rank coefficient has the wrong Möbius orientation. This converts the abstract gauge into a sharp obstruction to interpreting FD-144's test-count lower bound without an ancestry-connectivity hypothesis.

No external theorem is load-bearing. The proof is the elementary identity (10), so `SOURCES.md` requires no update.

## 9. Falsifiable next test

The next useful threshold problem should explicitly add an anchoring condition instead of merely increasing the test budget. A minimal model is:

- the visible ancestry graph contains at least one seeded coefficient vertex;
- every coefficient vertex whose recovery is requested lies in the same visible connected component as that anchor;
- observations remain source-independent and are restricted to source-native ancestry/Farey data.

Then ask whether a quantitative lower bound such as FD-144 survives after connectivity is guaranteed, or whether one can construct a source-native observable whose information budget is `O(r_T)` or smaller and whose anchored component equations are coercive.

A concrete falsifier of the present interpretation would be an ancestry-defect-only functional using **only edges with parent rank `>R_0`** that distinguishes (2) from Möbius. Such a functional cannot exist if it depends solely on the raw defect vector, because that vector is identically zero for both sources. Any successful discriminator must therefore import information not present in those high-rank edge defects: an anchor, a bridge, direct coefficients, or a genuinely nonlocal observable.

## Conclusion

FD-143 and FD-144 progressively enlarged the class and budget of local ancestry observations that one common source can fool. FD-145 identifies a more basic obstruction that survives even after the budget restriction is removed:

\[
\boxed{
\text{high-rank relative ancestry data}
\;\not\Rightarrow\;
\text{absolute Möbius orientation}
}
\tag{23}
\]

unless the measured component is connected to an anchor.

For the current Farey-discrepancy program, the immediate frontier is therefore **anchor connectivity before observation count**. Only after the source-native observable transports orientation from a Möbius-fixed region into the high-rank component does it make sense to ask whether the `o(r_T)` barrier of FD-144 is sharp.