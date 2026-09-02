# Shared-source full-packing constraint weave

![Simultaneous full-packing constraints in corrected shared-source coordinates](shared-source-full-packing-constraints.png)

## Question

When two positive-defect full-packed Ramanujan interactions share the same source prime `p` at one observation length `N`, can their exact row-kernel modes coexist in the shared `p`-frequency coordinates? The original visualization exposed a strong finite rigidity pattern, but it used unsigned nearest-boundary charts and therefore left a coordinate question for complement boundaries. `WI-104` has now resolved that issue exactly.

## Construction

For a close-prime pair `p<q<2p`, write `d=q-p`, `t=p-d`, and reduce the observation length to the nearest pairwise boundary
\[
\delta=\min\{N\bmod pq,\ pq-(N\bmod pq)\}.
\]
In the full-packing regime of `WI-096`/`WI-102`, the canonical short-boundary chart has
\[
\delta=kq+s,\qquad R=s-d=[kd]_p,\qquad g=\gcd(R,t)>1.
\]

The load-bearing correction from `WI-104` is that a complement boundary does not live in the same source coordinates as the direct short block. If
\[
\varepsilon=
\begin{cases}
+1,&N\bmod pq=\delta,\\
-1,&N\bmod pq=pq-\delta,
\end{cases}
\]
then the complement case contributes a source-side diagonal phase, which translates the residue-kernel chart. The actual deleted-interval start is
\[
\rho=
\begin{cases}
R,&\varepsilon=+1,\\
t-R,&\varepsilon=-1,
\end{cases}
\]
and the actual forced-zero interval is
\[
C=\{\rho,\ldots,\rho+d-1\}.
\]

On the complement of `C`, unwrap the source residues to the integer interval
\[
I=[\rho-t,\rho-1].
\]
`WI-104` proves that every full-packed kernel vector is exactly
\[
f(j)=F(w\bmod g),\qquad w\in I,\ j=w\bmod p,
\]
with `f=0` on `C` and `sum_x F(x)=0`. Thus the colored labels in the image are quotient-character coordinates, not a numerical rank embedding.

The rendered exact example keeps the earlier parameters
\[
p=47,\qquad N=95{,}384.
\]
For `q_1=59`,
\[
d_1=12,\quad \rho_1=28,\quad t_1=35,\quad g_1=7,
\]
so `C_1={28,...,39}`. For `q_2=61`,
\[
d_2=14,\quad \rho_2=27,\quad t_2=33,\quad g_2=3,
\]
so `C_2={27,...,40}`. Both actual intervals have center
\[
c=\rho_i+\frac{d_i}{2}=34.
\]

The first two rows show the exact quotient labels `w mod g_i` outside each deleted interval. The bottom row superposes the two equality systems: source residues belonging to the same quotient class are unioned, and any resulting component touching either forced-zero interval is killed.

## Observation

The corrected picture is simpler than the original unsigned-chart interpretation. The two actual holes are nested around one common center, and the combined equality system propagates the zero constraint through every source direction. In this example the large free component contains sites forced to zero by the other interaction, so all of its quotient-character degrees of freedom collapse; the remaining deleted sites are already zero individually.

More importantly, `WI-104` proves that the common-center phenomenon is not special to this example. For every simultaneous pair at one odd source prime,
\[
2c_i\equiv N\pmod p,
\]
and since each actual center lies strictly between `0` and `p`, all actual centers coincide. The earlier apparent “concentric or antipodal” alternative belonged to unsigned canonical short-boundary charts before the complement-boundary source phase was restored.

## Robustness

The current geometric statements are exact and do not depend on rendering resolution, color, floating-point rank thresholds, or a favorable finite sweep. `WI-104` proves both the corrected source-coordinate translation and
\[
K_1\cap K_2=\{0\}
\]
for any two distinct simultaneous positive-defect full-packed close-prime targets sharing one source prime and one observation length. Its proof reduces the common exterior to a finite word with two periods; the Fine--Wilf theorem supplies the common period, and a forced-zero collar meets every common-period class.

The earlier finite enumeration remains useful as historical motivation, but its mixed-sign geometry should not be used as evidence independently of the source-phase correction. The theorem now supersedes that exploratory coordinate interpretation.

## Research consequence

The motivating clue [[research/weil_inertia/clues/CLUE-full-packing-orbit-quotient-characters]] is resolved by [[research/weil_inertia/findings/WI-104-simultaneous-full-packed-prime-defects-have-trivial-shared-source-intersection]].

This visualization is retained only as an explanatory view of that exact result. It is not independent evidence, and it does not create a new clue or finding.
