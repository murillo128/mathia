# Visual-exploration source anchors

This file records durable external literature dependencies used to support or delimit canonical findings in `research/visual_exploration/`. It is an anchor list, not search history.

## Invariant-subspace perturbation geometry

- Chandler Davis and W. M. Kahan, **The Rotation of Eigenvectors by a Perturbation. III**, *SIAM Journal on Numerical Analysis* 7:1 (1970), 1–46. DOI: `10.1137/0707001`. Role: classical reference for principal angles and perturbation of invariant subspaces; prior-art boundary for the projector-angle language used in `VIS-005`. The commutator lower bound in that finding is elementary and is not claimed as a new general perturbation theorem.

## Reciprocal-prime asymptotics

- Franz Mertens, **Ein Beitrag zur analytischen Zahlentheorie**, *Journal für die reine und angewandte Mathematik* 78 (1874), 46–62. DOI: `10.1515/crll.1874.78.46`. Role: classical reciprocal-prime asymptotic underlying the shifted sieve product `prod_{7<=p<=x}(1-1/(p-2)) = Theta(1/log x)` in `VIS-005`; the shift from `p` to `p-2` changes the logarithm only by an absolutely convergent `O(sum_p p^-2)` correction.
